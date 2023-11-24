'''
36,2.5,SayText.py,SayText,9,,,0
move_num, duration, python_file, move_name, prec, post, mand.
'''
import os
import time
import pandas as pd
import numpy as np
from nao import Move

def eval_conditions(st):
    if pd.isna(st):
        return dict()
    st = st.replace(";",",")
    return eval(st)

directory = "dance_moves//"

#read metadata file and initialize all states
metadata = pd.read_csv('meta_data//MetaData-Duration.csv')
file_list = os.listdir('dance_moves')
ip = "127.0.0.1"
port = 49436

moves = dict()
# for index, row in metadata.iterrows():
#     #name, duration, preconditions, postconditions,popularity
#     moves[row['MoveName'][:-3]]=(Move(row['MoveName']+'.py',row['MoveName'],float(row['Duration'])))

move1 = 'AirGuitar'
move2 = 'SitRelax'
move3 = 'Clap'

metadata['Precond'] = np.nan
metadata['Postcond'] = np.nan
print(metadata)
exit()
try:
    start_time = time.time()
    print("RUNNING " + move1)
    os.system("python " + directory + move1 + ".py " + ip + ' ' + str(port))
    print("RUNNING " + move3)
    os.system("python " + directory + move2 + ".py " + ip + ' ' + str(port))
    supposed_duration = time.time()-start_time
    actual_duration = moves[move1].duration+moves[move2].duration
    if supposed_duration + 3 < actual_duration:
        pass
except Exception as e:
    print("Error creating broker:", e)