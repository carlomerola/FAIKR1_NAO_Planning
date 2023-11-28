'''
36,2.5,SayText.py,SayText,9,,,0
move_num, duration, python_file, move_name, prec, post, mand.
'''
import os
import time
import pandas as pd
import numpy as np
from nao import Move
from utils import *

def eval_conditions(st):
    if pd.isna(st):
        return dict()
    st = st.replace(";",",")
    return eval(st)

directory = "dance_moves//"

#read metadata file and initialize all states
read_df = pd.read_csv("meta_data//MetaData-Duration.csv", sep=";")
file_list = os.listdir('dance_moves')
config = get_config()

'''
TO DELETE

metadata = pd.read_csv("meta_data//MetaData-Duration.csv")
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

ip = "127.0.0.1"
port = 49436

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
'''

support_list = []
for i, rows in read_df.iterrows():
    '''
    if i == 2:
        break
    '''
    
    entry_mv1= {}
    entry_mv1['Duration'] = read_df['Duration'][i]
    entry_mv1['MoveName'] = read_df['MoveName'][i]
    entry_mv1['Precond'] = {}
    entry_mv1['Postcond'] = {}
    
    for j, rows2 in read_df.iterrows():
        #if same move, skip
        if i == j:
            continue
        '''
        if j == 2:
            break
        '''
        entry_mv2= {}
        entry_mv2['Duration'] = read_df['Duration'][j]
        entry_mv2['MoveName'] = read_df['MoveName'][j]
        

        '''
        TEST 
        
        entry_mv2= {}
        entry_mv2['MoveName'] = 'SitRelax.py'
        entry_mv2['Duration'] = 19.806
        entry_mv1['Precond'] = {}
        entry_mv1['Postcond'] = {}
        '''
        
        try:
            start_time = time.time()
            
            print("RUNNING " + entry_mv1['MoveName'])
            os.system("python " + directory + entry_mv1['MoveName']  + ' ' + config['ip'] + ' ' + str(config['port']))
            
            print("RUNNING " + entry_mv2['MoveName'])
            os.system("python " + directory + entry_mv2['MoveName']  + ' ' + config['ip'] + ' ' + str(config['port']))
            actual_duration = time.time()-start_time
            supposed_duration = entry_mv1['Duration'] + entry_mv2['Duration']
            
            if supposed_duration + 2 < actual_duration:
                entry_mv1['Postcond'][ ( 'compatible_' + entry_mv2['MoveName'] ) ] = False
                
        except Exception as e:
            print("Error creating broker:", e)
        
        
    support_list.append(entry_mv1)
print_df = pd.DataFrame().from_records(support_list)
print_df.to_csv("meta_data//MetaData-Conflicts.csv", sep=";")
    
print('PRINTING MOVE ENTRIES:')
print(support_list)
        