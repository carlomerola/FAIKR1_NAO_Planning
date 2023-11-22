from aima.search import *


def remove_possible_move(move_name, possible_moves):
    return tuple([i for i in possible_moves if i.name != move_name])

class Move():
    def __init__(self, file_name, name, duration, preconditions={},
                 postconditions={}, mandatory=0):
            self.file_name = file_name
            self.name = name
            self.duration = duration
            self.preconditions = preconditions
            self.postconditions = postconditions
            self.mandatory = mandatory


class Nao(Problem):
    def __init__(self, initial, goal):
        #initial - (move, pos_moves,time)
        self.initial = initial
        self.goal = goal
        Problem.__init__(self, initial, goal)


    def is_valid(self,state, possible_move):
        #if time is longer
        if state[2]  < possible_move.duration:
            return False
        #if postconditions from previos move dont go with precond of current move
        return self.precond_satisfied(state, possible_move)

    def precond_satisfied(self,current_move, possible_move):
        for key, value in possible_move.preconditions.items():
            if value == False:
                if key not in current_move.postconditions:
                    return False
                elif current_move.postconditions[key] != value:
                    return False
            else:
                if key not in current_move.postconditions:
                    continue
                elif current_move.postconditions[key] != value:
                    return False

        return True


    def successor(self, state):
        successors = dict()

        current_move, possible_moves, time_constrained = state  # retrieve the state
        possible_moves = remove_possible_move(current_move.name,possible_moves)

        for possible_move in possible_moves:
            if self.is_valid(state,possible_move):
                successors[possible_move.name] = (possible_move,
                                                  possible_moves,
                                                  time_constrained-possible_move.duration)

        return successors

    def goal_test(self, state):
        current_move, possible_moves, time_constrained = state
        return time_constrained < 4 and self.precond_satisfied(current_move,self.goal)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]

    def path_cost(self, c, state1, action, state2):
        return state2[1]





