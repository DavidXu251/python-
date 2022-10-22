import sounddevice as sd
import queue
import numpy as np


length=300
channels=1
q=queue.Queue()
plotdata=np.zeros((length, channels))
def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread)
        for each audio block."""
    if status:
        print(status, file=sys.stderr)
    # Fancy indexing with mapping
    #creates a (necessary!) copy:
    q.put(indata[:])
    print(indata)



stream = sd.InputStream(
        channels=1,#device
        samplerate=44100, callback=audio_callback)
