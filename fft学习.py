
import sounddevice as sd
rate=44100
stream=sd.InputStream(
    samplerate=rate,
    channels=1,
    dtype='float32',
)
stream.start()

import numpy as np
import matplotlib.pyplot as plt
fig, (ax1, ax2, ax3)=plt.subplots(3,1)

size=rate//5
while True:
    data,ok = stream.read(size)
    data=data[:, 0]
    ax1.set_ylim([-0.2, 0.2])
    ax1.plot(data)

    fft=np.fft.fft(data)
    ax2.set_ylim([-0.1,100])
    ax2.plot(np.log(np.linspace(0.01,1,size//2)),
                    abs(fft[:size//2]))
    
    data2=np.fft.ifft(fft)
    ax3.set_ylim([-0.2, 0.2])
    ax3.plot(data2.real)
    
    plt.pause(0.01)
    [x.cla() for x in [ax1,ax2,ax3]]
