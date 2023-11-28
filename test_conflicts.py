import os
import time
import pandas as pd
import numpy as np
from nao import Move
from utils import *

read_df = pd.read_csv("meta_data//MetaData-Duration.csv", sep=";")
file_list = os.listdir('dance_moves')
config = get_config()

support_list = []

entry_mv1= {}
entry_mv1['Duration'] = 2.902
entry_mv1['MoveName'] = 'SayOneMoreTime.py'
entry_mv1['Precond'] = {}
entry_mv1['Postcond'] = {}

entry_mv2= {}
entry_mv2['Duration'] = 9.949
entry_mv2['MoveName'] = 'RotationfootRLeg.py'


start_time = time.time()
    
print("RUNNING " + entry_mv1['MoveName'])
os.system("python " + directory + entry_mv1['MoveName']  + ' ' + config['ip'] + ' ' + str(config['port']))

print("RUNNING " + entry_mv2['MoveName'])
os.system("python " + directory + entry_mv2['MoveName']  + ' ' + config['ip'] + ' ' + str(config['port']))
actual_duration = time.time()-start_time
supposed_duration = entry_mv1['Duration'] + entry_mv2['Duration']

if supposed_duration + 2 < actual_duration:
    entry_mv1['Postcond'][ ( 'compatible_' + entry_mv2['MoveName'] ) ] = False

print("ENTRY MOVE 1:", entry_mv1)