import pyttsx3
from sensors import read_flex_sensors
from gesture_logic import recognize_gesture

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

print("🧤 Glove-Based Sign Language Translation System")

while True:
    flex_data = read_flex_sensors()
    gesture = recognize_gesture(flex_data)

    print("Recognized Gesture:", gesture)

    if gesture != "UNKNOWN":
        engine.say(gesture)
        engine.runAndWait()

    if input("Continue? (y/n): ").lower() != "y":
        break
