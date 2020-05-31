#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyaudio
import wave
import os
import datetime


# In[ ]:


now = datetime.datetime.now()
filename = 'Wave_' + str(now)[:10] + now.strftime("_%H_%M_%S.wav")


# In[ ]:


#The following code comes from markjay4k as referenced below
form_1 = pyaudio.paInt16
chans = 1
samp_rate = 44100
chunk = 512
record_secs = 15     #record time
dev_index = 2
wav_output_filename = filename


# In[ ]:


audio = pyaudio.PyAudio()


# In[ ]:


#setup audio input stream
stream = audio.open(format = form_1,
                  rate=samp_rate,
                  channels=chans, 
                  input_device_index = dev_index, 
                  input=True, 
                  frames_per_buffer=chunk)


# In[ ]:


print("recording")
frames = []

for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data=stream.read(chunk,exception_on_overflow = False)
    frames.append(data)

print("finished recording")


# In[ ]:


stream.stop_stream()
stream.close()
audio.terminate()


# In[ ]:


#creates wave file with audio read in
#Code is from the wave file audio tutorial as referenced below
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()


# In[ ]:


#plays the audio file
os.system("aplay test1.wav")

