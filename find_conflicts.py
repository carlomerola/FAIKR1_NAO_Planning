'''
ATTEMPT to find conflicts between moves by running them in sequence and checking execution time.
If the execution time is longer than the sum of the durations of the moves, then the robot is
falling, meaning the two moves are not compatible.
'''
import os
import time
import pandas as pd
import numpy as np
from nao import Move
from utils import *

#read metadata file and initialize all states_____________________
read_df = pd.read_csv("meta_data//MetaData-Duration.csv", sep=";")
config = get_config()
moves_directory = config['dance_moves_folder_location']
file_list = os.listdir(moves_directory)

support_list = []
for i, rows in read_df.iterrows():
    #get move1 metadata___________________________
    entry_mv1= {}
    entry_mv1['Duration'] = read_df['Duration'][i]
    entry_mv1['MoveName'] = read_df['MoveName'][i]
    entry_mv1['Precond'] = {}
    entry_mv1['Postcond'] = {}
    
    for j, rows2 in read_df.iterrows():
        #if same move, skip
        if i == j:
            continue
        
        #get move2 metadata___________________________
        entry_mv2= {}
        entry_mv2['Duration'] = read_df['Duration'][j]
        entry_mv2['MoveName'] = read_df['MoveName'][j]    

        try:
            #initialize time0______
            start_time = time.time()
            
            print("RUNNING " + entry_mv1['MoveName'])
            os.system("python " + moves_directory + entry_mv1['MoveName']  + ' ' + config['ip'] + ' ' + str(config['port']))
            
            print("RUNNING " + entry_mv2['MoveName'])
            os.system("python " + moves_directory + entry_mv2['MoveName']  + ' ' + config['ip'] + ' ' + str(config['port']))
            
            #calculate move1 + move2 duration. If > than move1 + move2 in metadata (NAO falling) insert incompatibility_____
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
        