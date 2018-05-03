
from glob import glob
from random import randint
import subprocess
import random
import time

# This is the folder with the MP3s. Make sure to enter the full path
predpath="/home/pi/Desktop/predatory"



def playsound(flag):
    if flag:
        filelist=glob(predpath+"/*.mp3")
        count=len(filelist)
        #print "COUNT:"
        #print count
        index=randint(0,count-1)
        print filelist[index]
        subprocess.call(["ffplay",filelist[index],"-autoexit"])
        #p=vlc.MediaPlayer("file://"+filelist[index])
        #p=MediaPlayer(path.join(cwd, "data\pred\Recording.m4a"))
        #p.play()
        #while p.get_state() == vlc.State.Playing:
        #    print "Here"
        #    time.sleep(1)
        #time.sleep(2)

# This function takes a boolean True/False argument
