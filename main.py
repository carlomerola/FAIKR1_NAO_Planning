import os
import threading
import re
from utils import *

def play_music(path,event):  # music playback by subprocess
    #playsound.playsound(path) runs longer that ~130 seconds (the duration of the song)
    playsound.playsound(path)
    print('Done')
    event.set()


def main(config,event):
    """
    1. Run the algorithm and create dance choreograph as a path of states
    2. Run the dance choreographe on the simulator
    """
    start_time = time.time()
    moves = get_moves_metadata(config)
    #get list of states (path) that represents the choreographe
    path = get_path(config,moves)
    # run the states on the simulator
    for move_name in path:  # for each element of final_path
        print(move_name)
        print('running: ' + move_name)
        if 'Say' in move_name:
            text = re.sub(r"(\w)([A-Z])", r"\1 \2", move_name[3:])
            os.system("python " + os.path.join(config["dance_moves_folder_location"],'SayText.py') + " " + config['ip'] + ' ' + str(config['port']) + ' "' + text + '"')
        else:
            os.system("python " + os.path.join(config["dance_moves_folder_location"],moves[move_name].file_name) + " " + config['ip'] + ' ' + str(config['port']))
        print(time.time()-start_time)
    event.set()

if __name__ == "__main__":
    config = get_config()
    finish_event = threading.Event()
    music_thread = threading.Thread(target=play_music, args=(os.path.join(config['directory'],config['music_location']),finish_event))
    music_thread.start()
    main_thread = threading.Thread(target=main, args=(config, finish_event))
    main_thread.start()
    finish_event.wait()

