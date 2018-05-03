
# coding: utf-8

# In[1]:


from keras.models import load_model
from keras.layers import Convolution2D
from librosa import load, feature
from os import getcwd, path
from glob import glob
from random import randint
from struct import unpack
from sys import exit
import subprocess
import tensorflow
import pyaudio
import wave
import numpy as np
import time

# In[2]:

# Path Setup, using absolute paths, meant for files to be directly on desktop of RBPi
cwd = "/home/pi/Desktop"
predpath="/home/pi/Desktop/predatory"

# Import trained model, must exist for code to function
try:
    model=load_model(path.join(cwd, 'model.h5'))
except OSError:
    exit("No model detected, closing...")
    
# Audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000  #fs
CHUNK = 1024  #samples
RECORD_SECONDS = 1.2
THRESHOLD=0
WAVE_OUTPUT_FILENAME = "file.wav"


# In[3]:


# Prection code, runs input through weights file, somewhat quick
def predict(file):
    y, sr = load(file, duration=1)  
    ps = feature.melspectrogram(y=y, sr=sr)
    test = np.array([ps.reshape( (128, 44, 1) )])
    (notWood, Wood) = model.predict(test)[0]
    prediction = True if Wood > .03 else False
	
	#Watch this value while sampling, may want to change threshold in line above to what is appropriate for model
    print("Predicting with: ", Wood)
    playsound(prediction)


# In[4]:


# Cannot get VLC to work on Pi, should look for faster implementation to play audio, subprocess is slow
def playsound(flag):
    if flag:
        filelist=glob(predpath+"/*.mp3")
        count=len(filelist)
        index=randint(0,count-1)
        print("Playing Sound...")
		print filelist[index]
        subprocess.call(["ffplay",filelist[index],"-autoexit"])
		print("Played Sound")
        #p=vlc.MediaPlayer("file://"+filelist[index])
        #p=MediaPlayer(path.join(cwd, "data\pred\Recording.m4a"))
        #p.play()
        #while p.get_state() == vlc.State.Playing:
        #    print "Here"
        #    time.sleep(1)
        #time.sleep(2)


# In[5]:


# TODO: Audio threshold to save power consumption on required predictions
while True:
	audio = pyaudio.PyAudio()
	stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=False, frames_per_buffer=CHUNK)
	print("Recording...")
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK, exception_on_overflow=False)
		frames.append(data)
	print("Finished recording")
 
	# Stop Recording, save audio to file on desktop
	# TODO: may want to look for more direct approach rather than rewriting file
	stream.stop_stream()
	stream.close()
	audio.terminate()
	waveFile = wave.open(path.join(cwd, WAVE_OUTPUT_FILENAME), 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
	predict(path.join(cwd, WAVE_OUTPUT_FILENAME))

