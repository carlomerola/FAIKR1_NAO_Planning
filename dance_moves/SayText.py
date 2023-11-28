import time
from naoqi import ALProxy
import sys


def main(robotIP, port,text):
    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
        ttsProxy.say(text)

    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e

    time.sleep(3)

if __name__ == "__main__":

    robotIP = sys.argv[1]
    port = int(sys.argv[2])
    if len(sys.argv) <= 3:
        text = 'Woo'
    else:
        text = sys.argv[3]

    main(robotIP, port,text)
