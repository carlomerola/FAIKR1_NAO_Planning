import pandas as pd
from nao import Move, Nao
import sys
import time
import playsound
from aima.search import *

def get_config():
    config={}
    robot_ip = "127.0.0.1"
    port = 9559
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]
    elif len(sys.argv) == 2:
        robot_ip = sys.argv[1]
    config['ip'] = robot_ip
    config['port'] = port
    config['directory'] = os.getcwd()
    config.update({'dance_moves_folder_location': 'dance_moves',
                   'metadata_file_location': 'meta_data//metadata.csv',
                   'music_location': 'tequila.mp3'
                   })
    return config


def play_music(path):  # music playback by subprocess
    playsound.playsound(path)


def eval_conditions(st):
    if pd.isna(st):
        return dict()
    st = st.replace(";", ",")
    return eval(st)


def get_moves_metadata(config):
    metadata = pd.read_csv(config['metadata_file_location'])
    moves = dict()
    for index, row in metadata.iterrows():
        # name, duration, preconditions, postconditions,popularity
        moves[row['MoveName']] = (Move(row['File'], row['MoveName'], float(row['Duration']),
                                       eval_conditions(row['Precond']), eval_conditions(row['Postcond']),
                                       row['Mandatory']))

    return moves


def get_path(config, moves):
    path = []

    transition_moves = [val for key, val in moves.items() if val.mandatory == 0 and key not in
                        ['Diagonalleft', 'Diagonalright', 'SayText', 'Clap']]

    # define order and time frame for mandatory states
    # state representation = initial, goal, time_constrained, possible_moves
    pairs_start_goal = [('StandInit', 'Hello', 8), ('Hello', 'StandZero', 8), ('StandZero', 'SitRelax', 9),
                        ('Diagonalleft', 'Stand', 7), ('Stand', 'Sit', 7), ('Diagonalleft', 'WipeForehead', 4),
                        ('WipeForehead', 'Crouch', 9)]

    # begin itteration
    path.append(pairs_start_goal[0][0])
    for (starting_state_name, goal_state_name, time_constraint) in pairs_start_goal:
        # generate the solution via search algorithm
        start_time = time.time()
        n = Nao(initial=(moves[starting_state_name], tuple(transition_moves), time_constraint),
                goal=moves[goal_state_name])
        answer = uniform_cost_search(n, lambda n: n.path_cost)
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
    phrase, next_move = ('WaitForIt','Diagonalleft') if move_name != 'Sit' else ('OneMoreTime','Diagonalright')
    path.append('Say' + phrase)
    path.append(move_name)
    path.append('SayTequila')
    path.append(next_move)
    path.append('Clap')
    return path

def crouch_and_say_tequila(move,path):
    path.append(move)
    path.append('SayTequila')
    return path