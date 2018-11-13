import speech_recognition as speech_recognition

AUDIO_FILE = ("example.wav")

r=sr.Recognizer()

with sr.Audiofile(AUDIO_FILE) as source:

	audio=r.record(source)

try:
	print("The audio file contains:" + r,recognize_google(audio))

except sr.UnkownValueError:
	print("google Speech Recognition could not understand audio")

except sr.RequestError as e:
	print("could not request results from google speech recognition service;{0}".format())
	