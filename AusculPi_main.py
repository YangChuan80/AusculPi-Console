#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyaudio

import numpy as np

import wave
import os
import datetime

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import messagebox


# In[2]:


'''
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
'''


# In[3]:


#The following code comes from markjay4k as referenced below
chunk = 512
samp_rate = 44100

form_1 = pyaudio.paInt16
chans = 1

record_secs = 30     #record time
dev_index = 2


# In[4]:


def about():
    messagebox.showinfo("About", "Author & Coder: Chuan Yang")


# In[5]:


def replay():
    #plays the audio file
    os.system("aplay " + filename_wav)    


# In[6]:


def button_callback(channel):
    global frames, frames_numpy, filename_wav, filename_png, filename_np
    
    text_status.delete('1.0', tk.END)
    text_status.insert('1.0', "Button was pushed!")     
    #print("Button was pushed!")

    now = datetime.datetime.now()
    filename_wav = 'Wave_File_' + str(now)[:10] + now.strftime("_%H_%M_%S.wav")
    filename_png = 'Chart_File_' + str(now)[:10] + now.strftime("_%H_%M_%S.png")
    filename_np = 'Array_File_' + str(now)[:10] + now.strftime("_%H_%M_%S")
    wav_output_filename = filename_wav
    png_output_filename = filename_png
    np_output_filename = filename_np
    

    p = pyaudio.PyAudio()

    #setup audio input stream
    stream = p.open(format = form_1,
                    rate=samp_rate,
                    channels=chans,
                    input_device_index = dev_index,
                    input=True,
                    frames_per_buffer=chunk)

    # the code below is from the pyAudio library documentation referenced below
    #output stream setup
    player = p.open(format = form_1,
                    rate=samp_rate,
                    channels=chans,
                    output=True,
                    frames_per_buffer=chunk)

    text_status.delete('1.0', tk.END)
    text_status.insert('1.0', "Broadcasting & Recording")     
    print("Broadcasting & Recording")
    frames = []
    frames_numpy = []

    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk,exception_on_overflow = False)
        frames.append(data)
    
        data_numpy = np.fromstring(data, dtype=np.int16)
        player.write(data_numpy, chunk)
        frames_numpy.append(data_numpy)
        
    text_status.delete('1.0', tk.END)
    text_status.insert('1.0', "Finished recording")     
    print("Finished recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    #creates wave file with audio read in
    #Code is from the wave file audio tutorial as referenced below
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(p.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

    #plays the audio file
    #os.system("aplay " + filename_wav)    
    
    # Export the plot:
    '''
    fig = plt.figure()
    s = fig.add_subplot(111)
    s.plot(frames_numpy)
    fig.savefig(png_output_filename, dpi=200)
    '''
    np.save(np_output_filename, frames_numpy)


# In[7]:


'''
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge


message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
'''


# In[8]:


root = tk.Tk()

root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.attributes('-fullscreen', True)
root.title('Auscul Pi -- A ear-contactless stethoscope')

# Text Editor
text_status = tk.Text(root, width=30, height=1, font=('tahoma', 30), bd=2, wrap='none')
text_status.place(x=50, y=20)

# Buttons

button_auscultate = tk.Button(root, text="Auscultate", width=20, font=('tahoma', 30), 
                         command=button_callback)
button_auscultate.place(x=50, y=100)

button_replay = tk.Button(root, text="Replay", width=20, font=('tahoma', 30), command=replay)
button_replay.place(x=50, y=200)

button_about = tk.Button(root, text="About...", width=12, font=('tahoma', 30), command=about)
button_about.place(x=600, y=100)

button_exit = tk.Button(root, text="Exit", width=12, font=('tahoma', 30), command=root.destroy)
button_exit.place(x=600, y=200)


root.mainloop()

