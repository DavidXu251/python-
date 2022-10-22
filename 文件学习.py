file=open('faded.m4a')
print(type(file))

import librosa
y,sr=librosa.load(file)
