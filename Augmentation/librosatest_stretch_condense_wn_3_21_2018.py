#Audio File Augmentation

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

import time


file_count = 0
stretch_count = 0
condense_count = 0
wn_count = 0

for audio_agment in range(0,120000): #number of files to create
    if file_count == 66:
        file_count = 0
    audio = MP3(r'C:\Users\Nick\Documents\COLLEGE SEMESTER 8\Senior Design\Woodpecker Drilling\input\0' + str(file_count) + ".mp3")
    file_count += 1
    audiolength = audio.info.length
    print("Total Time (sec): " + str(audio.info.length))
    outputbitrate = 0
    aug_select = 0
    print("aug reset to: " + str(aug_select))
    aug_select = random.randint(1,3)
    print("aug set to: " + str(aug_select))

    def load_audio_file(file_path):
        global outputbitrate
        data = librosa.core.load(file_path)[0]

        global stretch_count
        #stretch
        if aug_select == 1:
            rs = random.uniform(0.9, 1)
            print("rs: " + str(rs))
            stretch_data = librosa.effects.time_stretch(data, rs)
            stretch_count +=1

        global condense_count
        #condense
        if aug_select == 2:
            rc = random.uniform(1, 1.1)
            print("rc: " + str(rc))
            stretch_data = librosa.effects.time_stretch(data, rc)
            condense_count +=1

        global wn_count
        #Add white noise
        if aug_select == 3:
            w_noise = np.random.randn(len(data))
            rw = random.uniform(0.001, 0.005)
            print("rw: " + str(rw))
            stretch_data = data + rw*w_noise
            print("data_w_noise: " + str(stretch_data))
            wn_count +=1
        

        
        #set bit rate
        outputbitrate = (math.floor(len(data) / audiolength))
        print("test1: " + str(outputbitrate))
        input_length = (math.floor(len(data) / audiolength) * 5)
        print("input length: " + str(input_length))
        print("Total Size: " + str(len(data)))
        if len(data)>input_length:
            stretch_data = stretch_data[:input_length]
        else:
            #print(input_length)
            stretch_data = np.pad(stretch_data, (0, max(0, input_length - len(data))), "constant")
        return stretch_data

        
    #need to concatinate if file under 5sec...



    #Call Function
    stretch_data = load_audio_file(r'C:\Users\Nick\Documents\COLLEGE SEMESTER 8\Senior Design\Woodpecker Drilling\input\0' + str(file_count) + ".mp3")
    print("test2: " + str(outputbitrate))
    scaled = np.int16(stretch_data/np.max(np.abs(stretch_data)) * 32767)
    millis = int(round(time.time()))


    #Create MP3 file
    write((r'C:\Users\Nick\Documents\COLLEGE SEMESTER 8\Senior Design\Woodpecker Drilling\output\woodpecker_' + str(millis) + "_" + str(file_count) + ".mp3") , outputbitrate, scaled)
    print("----------------------------------------------")

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("MP3 file augmentation complete.")
print("Stretch count: " + str(stretch_count))
print("Condense count: " + str(condense_count))
print("White Noise count: " + str(wn_count))
