import pyttsx3 as py
engine = py.init()


#_________________To check voices in the system
# for voice in engine.getProperty('voices'):
#     print(voice)

 #_____________to set other voice
# voices =  engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# ______________________To get and set rate/speed of the voice
# rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate', 100)

# ______________________To get and set lowed/volume of the voice
# volume = engine.getProperty('volume')
# print(volume)
engine.setProperty('volume', 50)

Text = str(input("Enter you speech: "))
engine.save_to_file(Text, 'Audio.mp3')

engine.say(Text)
engine.runAndWait()
engine.stop()