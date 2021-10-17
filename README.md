# Crust
![Alt Text](linux.png)
Crust is a voice assistant project planned to work with linux systems.


It is a project currently under development.

<h2>Installing required libraries</h2>

```
pip3 install requests
pip3 install gTTS
pip3 install pyautogui
pip3 install SpeechRecognition
pip3 install time
pip3 install sys
pip3 install wave
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
pip3 install pyaudio
```
<h1>Future release patch notes</h1>

**- The microphone perception area will be expanded.**
<br>
**- 15 custom commands will be added, including network scanning.**
<br>
**- Default shell will be assumed to be zsh.**
<br>
**- Necessary commands for cyber security area will be added.**
<br>
**- And most importantly, it will be with you when the face recognition service Crust v2 is released.**
<h1> So how does the sound recording system work? </h1>

In voice assistants that are used in general, a result is obtained by processing and interpreting the sound instantly
but this does not work well on linux systems.
So i use audio recording software i wrote myself.

``` python
import pyaudio
import wave
from array import array

FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=44100
CHUNK=1024
RECORD_SECONDS=3.7
FILE_NAME="out.wav"

audio=pyaudio.PyAudio() #instantiate the pyaudio

#recording prerequisites
stream=audio.open(format=FORMAT,channels=CHANNELS, 
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

#starting recording
frames=[]

for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
    data=stream.read(CHUNK)
    data_chunk=array('h',data)
    vol=max(data_chunk)
    if(vol>=500):
        print("something said")
        frames.append(data)
    else:
        print("nothing")
    print("\n")


#end of recording
stream.stop_stream()
stream.close()
audio.terminate()
#writing to file
wavfile=wave.open(FILE_NAME,'wb')
wavfile.setnchannels(CHANNELS)
wavfile.setsampwidth(audio.get_sample_size(FORMAT))
wavfile.setframerate(RATE)
wavfile.writeframes(b''.join(frames))#append frames recorded to file
wavfile.close()
```

**As you can see in the code above, the system is actually quite simple, your voice is recorded every 3.7 seconds, of course, this recording is 3.7 seconds long, so when one is full, a new one is recorded and written to a single audio file. will run the assistant.**

<h1>Who am I</h1>

I am Z3di0nn, I am 16 years old, I am a 10th grade student at Kemal Pireci Anatolian High School. My purpose in life is to contribute to my country in the field of cyber security and programming in the future. And I have to lay the foundations for my future career so I try to devote the necessary time to classes and cybersecurity.

**I will put a virus that I developed on github in the future, my purpose here will be for you to look at the source codes and see how simple android devices are hacked.**

