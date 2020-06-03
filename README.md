# Auscul Pi
A Low-Cost Ear-Contactless Stethoscope Powered by Raspberry Pi and Python.

***Chuan Yang*** (<yangc@sj-hospital.org>)

[![Windows Build status](https://img.shields.io/badge/Windows-passing-brightgreen.svg)](https://github.com/YangChuan80/WillowbendDICOM)
[![MIT license](https://img.shields.io/badge/license-MIT%20License-blue.svg)](LICENSE)
[![Dowloads](https://img.shields.io/badge/downloads-43M-green.svg)](https://github.com/YangChuan80/WillowbendDICOM/raw/master/Installer/WillowbendDICOM_Installer.exe?raw=true)
[![Medicine Application](https://img.shields.io/badge/application-medicine-red.svg)](README.md)
[![Home](https://img.shields.io/badge/GitHub-home-ff69b4.svg)](https://github.com/YangChuan80)

## Introduction
Since the outbreak of COVID-19, more and more physicians and nurses have been participating the battle to coronavirus at the first line treatment. Almost all patients in critical status were having pneumonia, respiratory failure and/or acute respiratory distress syndrome. So, auscultation was important for those patients to achieve accurate diagnosis, assessment of current severity and treatment efficacy. However, inside quarantine ward in hospitals, medical staff who were wearing protective clothing were unable to use conventional stethoscopes due to the head protective suit covering the regions of their ears. Auscultation examination was essential but hard to accomplished especially to the patients with poor respiratory conditions, such as severe pneumonia, respiratory dysfunction, intensive cases who were intubated and assisted with ventilators. Some experts have viewpoint suggesting less stethoscope and more ultrasound, while other experts stress the necessity of stethoscope and auscultation in COVID-19 treatment. 

To challenge this paradox circumstance, we developed an electronic stethoscope using a credit card sized single-board computer (SBC), Raspberry Pi, connected to a chest piece of a conventional stethoscope and a tiny speaker, which can be easily modified by medical staff themselves. The software run by raspberry pi coded in python programming language was open source and has already been published on GitHub repository. All users who are interest in the stethoscope all around the world can assemble the components easily and download the software freely in a do-it-yourself (DIY) way. 


## Installation from Source
This option is only adopted by Python specialist. There are several dependencies necessarily preinstalled in your Python interpreter:

- **PyAudio**
```
$ sudo apt install python3-pyaudio
 ```
Else if you are running python 2.7
```
$ sudo apt install python-pyaudio 
```

- **Pydicom** 1.0
 - Download pydicom source from [https://github.com/darcymason/pydicom](https://github.com/darcymason/pydicom)
 - Of course, also:
```
pip install pydicom
```

- **OpenCV**
 - The opencv should be the the latest version:
```
pip install opencv-python -U
```
After you complete the WillowbendDICOM.py file download, run it:
```
python WillowbendDICOM.py
```
Python interpreter have to be Python 3.4 or later.

- **Setuptools & Pyinstaler**
 - If you'd like to use **PyInstaller**, you should downgrade your **setuptools** module to **19.2**.

To perform frozen binary, do this:
```
pyinstaller WillowbendDICOM.py -w
```

## Instructions
- Click **Browse** button to choose the DICOM file(s). 
- Load this chosen file. Don't forget to press **Load** button. When file successfully loaded, a information dialog will pop up to notice you. 
- Click **Convert** button on the right to convert the currently loaded DICOM file to AVI file. During this session, you will be asked to specify the location you're going to output to. Click **OK**. You'll wait for about a second, and your AVI file is ready! Congratulations!
- Optionally, you can customize the value of the **Clip Limit** if you're not satisfied with your converted AVI file with the default value of 3.0. The higher value means the more contrast effect in the video file you'll get. 

## License
The MIT License (MIT)

Copyright (c) 2019 Chuan Yang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributor List
- [@wenzhexue](http://github.com/wenzhexue) (**Wenzhe Xue**, Ph.D., Mayo Clinic) 
