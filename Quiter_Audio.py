import os
import subprocess
import glob
from random import *
import random
from pydub import AudioSegment
import sys
import time

audio_dir = r'C:\Users\Nick\Documents\COLLEGE SEMESTER 8\Senior Design\Quieter Audio\Make_Quieter_Input\\'
extension_list = ('*.mp3')


for audio_augment in range(0,1):
    os.chdir(audio_dir)
    audiofileslist = glob.glob(extension_list)
    finalsong = AudioSegment.from_mp3(audio_dir + '00.mp3') #?
    finalsong = finalsong[:0]                               #?
    count = 0

    print(audiofileslist)
    
    for audio in audiofileslist:
        print(audio + " " + str(len(audio)) + "seconds")

        mp3_filename = os.path.splitext(os.path.basename(audio))[0] + '.mp3' 
        song = None
        song = AudioSegment.from_mp3(mp3_filename)
       # start_reduce_time = 0                         #pick how long to reduce from start of audio file
        #start_reduce_song = song[:start_reduce_time]                   #clasify object at start
        beginning_reduce_volume = song - 15   #1-10dB reduce
        add_audio = beginning_reduce_volume[:5000]

        finalsong += add_audio
        
        
        os.chdir(r'C:\Users\Nick\Documents\COLLEGE SEMESTER 8\Senior Design\Quieter Audio\Make_Quieter_Output')
        millis = int(round(time.time()))
        print("Exporting now")
        finalsong.export("0" + str(count) + ".mp3", format="mp3", bitrate="192k")
        os.chdir(audio_dir)
        
        count += 1
        finalsong = finalsong[:0]
