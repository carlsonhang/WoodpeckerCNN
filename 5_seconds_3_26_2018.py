import os
import subprocess
import glob
from random import *
import random
from pydub import AudioSegment
import sys
import time

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from subprocess import check_output

#Import stuff

import numpy as np
import random
import itertools
import librosa
from scipy.io.wavfile import write

import IPython.display as ipd
import matplotlib.pyplot as plt
import math

from mutagen.mp3 import MP3

audio_dir = r'C:\Users\Nick\Documents\COLLEGE SEMESTER 8\Senior Design\Woodpecker Drilling\1st_alg_input\\'
extension_list = ('*.mp3')

#for audio_augment in range(0,1):
os.chdir(audio_dir)
audiofileslist = random.sample(glob.glob("*"), len(glob.glob("*")))
finalsong = AudioSegment.from_mp3(audio_dir + '066.mp3') ###
finalsong = finalsong[:0]                               

print(audiofileslist)

total_length = 0
count = 0

for audio in audiofileslist:
    file = MP3(r'C:\Users\Nick\Documents\COLLEGE SEMESTER 8\Senior Design\Woodpecker Drilling\all_woodpecker_files\066' + ".mp3") ###
    audiolength = file.info.length
    if count == 0:
        print(audiolength)
    count += 1
    print("total_length:" + str(total_length))
    if total_length >= 5:                             
        finalsong = finalsong[:5000]
        os.chdir(r'C:\Users\Nick\Documents\COLLEGE SEMESTER 8\Senior Design\Woodpecker Drilling\1st_alg_output') 
        millis = int(round(time.time()))
        print("Exporting now")
        finalsong.export("066.mp3", format="mp3", bitrate="192k") ###
        exportedsong = MP3(r'C:\Users\Nick\Documents\COLLEGE SEMESTER 8\Senior Design\Woodpecker Drilling\1st_alg_output\066'+ ".mp3") ###
        final_length = exportedsong.info.length
        print(final_length)
        os.chdir(audio_dir)
        break
    else:
        mp3_filename = os.path.splitext(os.path.basename(audio))[0] + '.mp3' 
        song = None
        song = AudioSegment.from_mp3(mp3_filename)
        x = 5000
        add_audio = song[:x]
        finalsong += add_audio
        total_length += audiolength
 
#end concatination function

print("Complete")
