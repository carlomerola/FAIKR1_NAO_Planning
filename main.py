import os
import threading
import re
from utils import *


def main(config):
    start_time = time.time()
    moves = get_moves_metadata(config)
    path = get_path(config,moves)
    # iterate search algoritham to find best transitions between mandatory states
    for move_name in path:  # for each element of final_path
        print(move_name)
        print('running: ' + move_name)
        if 'Say' in move_name:
            text = re.sub(r"(\w)([A-Z])", r"\1 \2", move_name[3:])
            os.system("python " + "dance_moves//" + 'SayText.py' + " " + config['ip'] + ' ' + str(config['port']) + ' "' + text + '"')
        else:
            os.system("python " + "dance_moves//" + moves[move_name].file_name + " " + config['ip'] + ' ' + str(config['port']))
        print(time.time()-start_time)

if __name__ == "__main__":
    config = get_config()    
    music_thread = threading.Thread(target=play_music, args=(config['directory'] + "//"+config['music_location'],))
    music_thread.start()
    main(config)
    print (music_thread.join())