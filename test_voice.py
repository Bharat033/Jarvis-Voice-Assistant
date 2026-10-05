import pyttsx3

print("Starting voice test...")

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

print("Number of voices:", len(voices))

for i, voice in enumerate(voices):
    print(i, voice.name)

engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

print("Speaking now...")

engine.say("Ya, I am Jarvis.")
engine.runAndWait()

print("Voice test completed.")