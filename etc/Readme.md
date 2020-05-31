# 1. We should install the pyaudio module:  # ***** Essential *****!
$ sudo apt install python3-pyaudio

# 2. Check the hardware of record and play configuration:
$ arecord -l

$ aplay -l

find the card # and device #

For instance, the record is card 1 and device 0, and play is card 0 and device 0:

You also can use
$ lsusb
to display the USB port.

Make a system file name ".asoundrc":

pcm.!default {
  type asym
  capture.pcm "mic"
  playback.pcm "speaker"
}
pcm.mic {
  type plug
  slave {
    pcm "hw:1,0"
  }
}
pcm.speaker {
  type plug
  slave {
    pcm "hw:0,0"
  }
}

# 3. Setup several settings:
$ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev

# 4. Adjust the volume:
$ alsamixer

# 5. Configure the Raspberry Pi system:  # ********** Essential !!!!! ***************
$ sudo raspi-config

Select "Advanced Options", then select "Audio", press Enter. After that select "Finish".

# 6. Test the audio:
Speaker:
$ speaker-test –t wav

Microphone:
$ arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw sample.wav
aplay --format=S16_LE --rate=16000 sample.wav

# 7. Config Script Autorun in Raspberry Pi
1) Switch to root account

sudo su

2) Edit the file rc.local

sudo nano /etc/rc.local

3) Append a line before exit()

sudo python /xx/xx/xx.py

4) Save and reboot to take effect
5) Terminate the script

Open terminal and type:

top

to find the PID no, then type:

kill #PID NO

# Install GPIO Tactile Button Programme
$ sudo apt-get install python3-rpi.gpio