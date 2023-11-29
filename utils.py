import pandas as pd
from nao import Move, Nao
import sys
import time
import playsound
from aima.search import *
import configparser

def get_config():
    #read config file
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    config = parser['DEFAULT']
    if len(sys.argv) > 2:
        config['port'] = sys.argv[2]
        config['ip'] = sys.argv[1]
    elif len(sys.argv) == 2:
        config['ip'] = sys.argv[1]
    config['directory'] = os.getcwd()
    metadata_loc = config['metadata_file_location'].split('//')
    config['metadata_file_location'] = os.path.join(metadata_loc[0], metadata_loc[1])
    return config

def eval_conditions(st):
    if pd.isna(st):
        return dict()
    return eval(st)


def get_moves_metadata(config):
    metadata = pd.read_csv(config['metadata_file_location'],sep=';')
    moves = dict()
    for index, row in metadata.iterrows():
        # filename,movename, duration, preconditions, postconditions, mandatory
        moves[row['MoveName']] = (Move(row['FileName'], row['MoveName'], float(row['Duration']),
                                       eval_conditions(row['Precond']), eval_conditions(row['Postcond']),
                                       row['Mandatory']))

    return moves


def get_path(config, moves):
    """
    Iterations of uniform cost search to find best path (list of states) that satisfies the time constraint
    """
    path = []

    transition_moves = [val for key, val in moves.items() if val.mandatory == 0 and key not in
                        ['Diagonalleft', 'Diagonalright', 'SayText', 'Clap']]

    # define order and time frame for mandatory states
    # state representation = initial, goal, time_constrained, possible_moves
    pairs_start_goal = [('StandInit', 'Hello', 8), ('Hello', 'StandZero', 6), ('StandZero', 'SitRelax', 6),
                        ('Diagonalleft', 'Stand', 4), ('Stand', 'Sit', 6), ('Diagonalleft', 'WipeForehead', 4),
                        ('WipeForehead', 'Crouch', 8)]

    # begin itteration
    path.append(pairs_start_goal[0][0])
    for (starting_state_name, goal_state_name, time_constraint) in pairs_start_goal:
        # generate the solution via search algorithm
        while True:
            n = Nao(initial=(moves[starting_state_name], tuple(transition_moves), time_constraint),
                    goal=moves[goal_state_name])
            answer = uniform_cost_search(n, lambda n: n.path_cost)
            if answer != None:
                break
            time_constraint+=1
        print('Path cost: ' + str(answer.get_path_cost()))
        path += answer.solution()
        if 'sit' in goal_state_name.lower():
            path = sit_and_say_tequila(goal_state_name, path)
        elif 'crouch' in goal_state_name.lower():
            path = crouch_and_say_tequila(goal_state_name, path)
        else:
            path.append(goal_state_name)
        # remove the used transition moves for the next iteration
        transition_moves = [move for move in transition_moves if move.name not in path]
    print(path)
    return path

def sit_and_say_tequila(move_name,path):
    #special combinations of moves to ensure a WOW effect when the Tequila sections comes
    phrase, next_move = ('WaitForIt','Diagonalleft') if move_name != 'Sit' else ('OneMoreTime','Diagonalright')
    path.append('Say' + phrase)
    path.append(move_name)
    path.append('SayTequila')
    path.append(next_move)
    path.append('Clap')
    return path

def crouch_and_say_tequila(move,path):
    # special combinations of moves to ensure a WOW effect when the Tequila sections comes
    path.append(move)
    path.append('SayTequila')
    return path