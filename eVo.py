import speech_recognition as sr
import sys

import pyautogui
import time
#metni sese dönüştürmek için
from gtts import gTTS
#sistem dosyalarını daha rahat şekilde açmak için
import os




def main():
	evo = input(" > ")

def speak(data):
	tts = gTTS(text=data , lang='en')
	tts.save("audio.mp3")
	os.system("mpg123 audio.mp3 ")
	os.system("rm audio.mp3")


val = 5

while val == 5:

	os.system("python3 record1.py > test.txt")
	hellow=sr.AudioFile("out.wav")
	with hellow as source:
		r = sr.Recognizer()
		audio = r.record(source)
		try:
			z = r.recognize_google(audio, language="tr")



			s = z.replace("A", "a")
			s = z.replace("B", "b")
			s = z.replace("C", "c")
			s = z.replace("Ç", "ç")
			s = z.replace("D", "d")
			s = z.replace("E", "e")
			s = z.replace("F", "f")
			s = z.replace("G", "g")
			s = z.replace("Ğ", "ğ")
			s = z.replace("H", "h")
			s = z.replace("I", "ı")
			s = z.replace("İ", "i")	
			s = z.replace("J", "j")
			s = z.replace("K", "k")
			s = z.replace("L", "l")
			s = z.replace("M", "m")
			s = z.replace("N", "n")
			s = z.replace("O", "o")
			s = z.replace("Ö", "ö")
			s = z.replace("P", "p")
			s = z.replace("R", "r")
			s = z.replace("S", "s")
			s = z.replace("Ş", "ş")
			s = z.replace("T", "t")
			s = z.replace("U", "u")
			s = z.replace("Ü", "ü")
			s = z.replace("V", "v")
			s = z.replace("Y", "y")
			s = z.replace("Z", "z")
			s = z.replace("W", "w")
			s = z.replace("X", "x")



		except:
			pass
		try:
			print(s)
		except:
			pass




#os.system("ffmpeg -i file.mp3 -ar 16000 -ac 1 file.wav")
#os.system("python3 evo_v4.py")
#os.system("sox -t alsa default test.wav")




	if(s == "hello" or s == "hello "):
		speak("hello , I am evo your voice asistant")
		speak("How can I help you")


	elif("open" in s):
		argo = s.split()[-1] 

		z = argo.replace("A", "a")
		z = argo.replace("B", "b")
		z = argo.replace("C", "c")
		z = argo.replace("Ç", "ç")
		z = argo.replace("D", "d")
		z = argo.replace("E", "e")
		z = argo.replace("F", "f")
		z = argo.replace("G", "g")
		z = argo.replace("Ğ", "ğ")
		z = argo.replace("H", "h")
		z = argo.replace("I", "ı")
		z = argo.replace("İ", "i")	
		z = argo.replace("J", "j")
		z = argo.replace("K", "k")
		z = argo.replace("L", "l")
		z = argo.replace("M", "m")
		z = argo.replace("N", "n")
		z = argo.replace("O", "o")
		z = argo.replace("Ö", "ö")
		z = argo.replace("P", "p")
		z = argo.replace("R", "r")
		z = argo.replace("S", "s")
		z = argo.replace("Ş", "ş")
		z = argo.replace("T", "t")
		z = argo.replace("U", "u")
		z = argo.replace("Ü", "ü")
		z = argo.replace("V", "v")
		z = argo.replace("Y", "y")
		z = argo.replace("Z", "z")
		z = argo.replace("W", "w")
		z = argo.replace("X", "x")

		speak("Opening "+z+"")
		os.system(""+z+" &")


	elif(s == "uyan"):
		speak("Good Morning sir , How can ı help you")

	elif(s == "Google" or s == "google"):
		os.system("firefox --new-window www.google.com &")
		speak("Opening Google ")

	elif(s == "close Firefox" or s == "close firefox"):
		os.system("pkill -f firefox")



	elif("ara Google" in s):


		text = s
		words = text.split()
		data = "ara"
		data2 = "Google"
		data3 = "ifadesini"
		data4 = ""
		status = False

		for word in words:
			if word == data2:
				words.remove(word)
				status = True

		for word in words:
			if word == data:
				words.remove(word)
				status = True


		if status:
	   		text = ' '.join(words)
	   		r = text.replace(" " , "+")
	   		my_string = "firefox https://www.google.com/search?q="+r+" &"
	   		os.system(my_string)
	   		speak("Opening "+text+" possible outcomes are listed sir")


	elif("close" in s):


		argc = s.split()[-1]
		print(argc)

		b = argc.replace("A", "a")
		b = argc.replace("B", "b")
		b = argc.replace("C", "c")
		b = argc.replace("Ç", "ç")
		b = argc.replace("D", "d")
		b = argc.replace("E", "e")
		b = argc.replace("F", "f")
		b = argc.replace("G", "g")
		b = argc.replace("Ğ", "ğ")
		b = argc.replace("H", "h")
		b = argc.replace("I", "ı")
		b = argc.replace("İ", "i")	
		b = argc.replace("J", "j")
		b = argc.replace("K", "k")
		b = argc.replace("L", "l")
		b = argc.replace("M", "m")
		b = argc.replace("N", "n")
		b = argc.replace("O", "o")
		b = argc.replace("Ö", "ö")
		b = argc.replace("P", "p")
		b = argc.replace("R", "r")
		b = argc.replace("S", "s")
		b = argc.replace("Ş", "ş")
		b = argc.replace("T", "t")
		b = argc.replace("U", "u")
		b = argc.replace("Ü", "ü")
		b = argc.replace("V", "v")
		b = argc.replace("Y", "y")
		b = argc.replace("Z", "z")
		b = argc.replace("X", "x")
		b = argc.replace("W", "w")
		print(b)
		speak("Closing "+b+" ")
		os.system("pkill -f "+b+"")

	elif(s == "stop"):
		val = 1

	elif("Translate" in s):
		trans = s.split()[-1]
		os.system("firefox https://translate.google.com/?sl=en&tl=tr&text="+trans+"&op=translate &")
		speak("Translate "+trans+"")

	elif(s == "shut down"):
		os.system("shutdown -h 3")


	elif(s == "bekle"):
		time.sleep(150)


	elif("search YouTube" in s):

		text = s
		words = text.split()
		data = "YouTube"
		status = False

		for word in words:
			if word == data:
				words.remove(word)
				status = True
		if status:
   			text = ' '.join(words)
   			r = text.replace(" " , "+")
   			my_string = "firefox https://www.youtube.com/results?search_query="+r+" &"
   			os.system(my_string)

   			speak("Showing "+s+" possible videos sir")

	elif(s == "YouTube'u aç"):
		os.system("firefox www.youtube.com &")



	#elif(s == "belirlenen hedefleri taramaya başla"):

		#f = open('src/target.txt') 
		#targetline = f.readlines()
		#lenn = len(targetline)
		#line_num = targetline[0] # 1. line
		#f.close()

	#elif (s == "şifreleme Protokolü"):
		


	else:
		speak("Something wrong ")


