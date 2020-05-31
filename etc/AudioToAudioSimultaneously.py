#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyaudio
import numpy as np


# In[ ]:


# The following code comes from markjay4k as referenced below
chunk = 512
RATE = 44100


# In[ ]:


# Define the object
p = pyaudio.PyAudio()


# In[ ]:


# input stream setup
stream = p.open(format = pyaudio.paInt16,
                rate=RATE,
                channels=1, 
                input_device_index = 2, 
                input=True, 
                frames_per_buffer=chunk)

# the code below is from the pyAudio library documentation referenced below
#output stream setup
player = p.open(format = pyaudio.paInt16,
                rate=RATE,
                channels=1, 
                output=True, 
                frames_per_buffer=chunk)


# In[ ]:


while True:            #Used to continuously stream audio
    data = np.fromstring(stream.read(chunk,exception_on_overflow = False),dtype=np.int16)
    player.write(data,chunk)


# In[ ]:


#closes streams
stream.stop_stream()
stream.close()
p.terminate

