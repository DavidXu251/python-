

import numpy as np

sound=np.zeros((440*16,))
def add_freq(freq):
    global sound
    i=0
    while True:
        i+=1
        freq2=int(freq*i)
        if freq2>=len(sound):
            break
        print(freq2)
        sound[freq2-20 : freq2+20]+=1

add_freq(440)
add_freq(550)
add_freq(660)

import matplotlib.pyplot as plt
plt.plot(sound)
plt.show()



