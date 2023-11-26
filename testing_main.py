import sys
import os
from naoqi import ALProxy
import time
import numpy as np
import pandas as pd
from nao import Move

ip = "127.0.0.1"
port = 55609


# def precond_satisfied(current_move, possible_move):
#     for key, value in possible_move.preconditions.items():
#         if value==False:
#             if key not in current_move.postconditions:
#                 return False
#             elif current_move.postconditions[key]!=value:
#                 return False
#         else:
#             if key not in current_move.postconditions:
#                 continue
#             elif current_move.postconditions[key]!=value:
#                 return False
#
#     return True
#
# def eval_conditions(st):
#     if pd.isna(st):
#         return dict()
#     st = st.replace(";",",")
#     print(st)
#     return eval(st)
#
# #read meta data file and initialize all states
# metadata = pd.read_csv('meta_data//metadata.csv')
# path = []
#
# moves = dict()
# for index, row in metadata.iterrows():
#     #name, duration, preconditions, postconditions,popularity
#
#     moves[row['MoveName']]=(Move(row['File'],row['MoveName'],float(row['Duration']),
#                                      eval_conditions(row['Precond']),eval_conditions(row['Postcond']),
#                             row['SubjectiveVisualRating'], row['Mandatory']))
# moves['SayTequila'] = (Move("SayTequila.py","SayTequila",1))
# moves['SayOneMoreTime'] = (Move("SayOneMoreTime.py","SayOneMoreTime",1))
# moves['SayWaitForIt'] = (Move("SayWaitForIt.py","SayWaitForIt",1))
# transition_moves = [val for key,val in moves.items() if val.mandatory==0 and key not in
#                     ['Diagonalleft','Diagonalright','SayTequila','SayOneMoreTime','SayWaitForIt']]
# print(len(moves))
# print(precond_satisfied(moves['AirGuitar'],moves['SitRelax']))
# print(precond_satisfied(moves['AirGuitar'],moves['AirGuitar']))
# print(precond_satisfied(moves['AirGuitar'],moves['StandZero']))

try:
    start_time = time.time()
    os.system("python " + "dance_moves//" + 'Diagonalr ight.py' + " " + ip + ' ' + str(port))
    os.system("python " + "dance_moves//" + 'SitRelax.py' + " " + ip + ' ' + str(port))
    print(time.time()-start_time)
except Exception as e:
    print("Error creating broker:", e)

