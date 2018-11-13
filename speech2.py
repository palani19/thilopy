import speech_recognition as sr 
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic.energy.Threshold=True
	print("Say something")
	while True:
		audio = r.listen(source)
		print("You said" + r.recognize_google(audio))