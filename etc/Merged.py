import pyaudio
import numpy as np
import wave
import os
import datetime
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import matplotlib.pyplot as plt

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#The following code comes from markjay4k as referenced below
chunk = 512
samp_rate = 44100

form_1 = pyaudio.paInt16
chans = 1

record_secs = 30     #record time
dev_index = 2

def button_callback(channel):
    global frames, frames_numpy
    
    print("Button was pushed!")

    now = datetime.datetime.now()
    filename_wav = 'Wave_File_' + str(now)[:10] + now.strftime("_%H_%M_%S.wav")
    filename_png = 'Chart_File_' + str(now)[:10] + now.strftime("_%H_%M_%S.png")
    wav_output_filename = filename_wav
    png_output_filename = filename_png
    

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

    print("Broadcasting & Recording")
    frames = []
    frames_numpy = []

    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk,exception_on_overflow = False)
        frames.append(data)
    
        data_numpy = np.fromstring(data, dtype=np.int16)
        player.write(data_numpy, chunk)
        frames_numpy.append(data_numpy)

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
    os.system("aplay " + filename_wav)    
    
    # Export the plot:
    fig = plt.figure()
    s = fig.add_subplot(111)
    s.plot(frames_numpy)
    fig.savefig(png_output_filename, dpi=200)
    
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge


message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up