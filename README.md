# WoodpeckerCNN
Woodpecker classifier using CNN for Raspberry Pi:
-Directory "PiCode" contains necessary code specifically for Pi implementation
-Create model using the ConvNN notebook, easier to experiment with.
-Run test implementation with Test_v1 notebook on PC with microphone and speakers to test model before transfering to Raspberry Pi.
-Important: Make sure package version for Tensorflow, Keras, and maybe Librosa are the same as versions installable on the Raspberry Pi. If other errors occur on Pi, check version of other packages as well (Scipy and numpy for example).
