import time
import os
import pandas as pd
import numpy as np
from utils import *

config = get_config()


meta_data = []
directory = "dance_moves//"
file_list = os.listdir('dance_moves')

def calculate_duration(config,path):
    start_time = time.time()
    statement = "python " + path + " " + config['ip'] + " " + str(config['port'])
    os.system(statement)
    return round(float(time.time() - start_time),4)

'''
for file_name in file_list:
    entry = {}
    entry['MoveName'] = file_name
    entry['Duration'] = calculate_duration(config,directory+file_name)
    entry['Precond'] = np.nan
    entry['Postcond'] = np.nan
    meta_data.append(entry)
    
meta_df = pd.DataFrame().from_records(meta_data)
meta_df.to_csv("meta_data//MetaData-Duration.csv", sep=";")
print('File created')
'''

read_df = pd.read_csv("meta_data//MetaData-Duration.csv", sep=";")

support_list = []
for i, rows in read_df.iterrows():
    if i == 2:
        break
    
    entry_mv1= {}
    entry_mv1['MoveName'] = read_df['MoveName'][i]
    entry_mv1['Duration'] = read_df['Duration'][i]
    entry_mv1['Precond'] = {}
    entry_mv1['Postcond'] = {}
    
    for j, rows_2 in read_df.iterrows():
        if i == j:
            continue
        
        if j == 2:
            break
        
        '''
        CORRECT ONE
        
        entry_mv2= {}
        entry_mv2['MoveName'] = read_df['MoveName'][j]
        entry_mv2['Duration'] = read_df['Duration'][j]
        entry_mv1['Precond'] = {}
        entry_mv1['Postcond'] = {}
        '''
        
        '''
        TEST DOWN
        '''
        entry_mv2= {}
        entry_mv2['MoveName'] = 'SitRelax.py'
        entry_mv2['Duration'] = 19.806
        entry_mv1['Precond'] = {}
        entry_mv1['Postcond'] = {}
        
        try:
            start_time = time.time()
            
            print("RUNNING " + entry_mv1['MoveName'])
            os.system("python " + directory + entry_mv1['MoveName']  + ' ' + config['ip'] + ' ' + str(config['port']))
            
            print("RUNNING " + entry_mv2['MoveName'])
            os.system("python " + directory + entry_mv2['MoveName']  + ' ' + config['ip'] + ' ' + str(config['port']))
            actual_duration = time.time()-start_time
            supposed_duration = entry_mv1['Duration'] + entry_mv2['Duration']
            
            if supposed_duration + 3 < actual_duration:
                entry_mv1['Precond'].append( {( 'compatible_' + entry_mv2['MoveName'] ) : False} )
                
        except Exception as e:
            print("Error creating broker:", e)
        
        
    support_list.append(entry_mv1)
    
print('PRINTING MOVE ENTRIES:')
print(support_list)
        
    

'''
TEMPORARY 

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

'''
    
    
