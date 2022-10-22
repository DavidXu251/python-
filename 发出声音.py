import pyaudio
import math

# instantiate PyAudio (1)
p = pyaudio.PyAudio()
# open stream (2)
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    output=True,
    frames_per_buffer=1024)
i=0
while True:
    i+=1
    if i>=2*math.pi:
        i=0
    data=math.sin(i)
    data=bytes([data])
    stream.write(data)

