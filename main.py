
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',100)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def arriving_call():
    train_no = input("enter the train number: ")
    from_station = input("station comming from: ")
    via_stations = input("Via stations: ")
    to_station = input("station going to: ")
    train_name = input("Train name: ")
    platform_number = input("Enter platform number: ")
    train_no_sort = ""
    for i in train_no:
        train_no_sort = train_no_sort+" "+i

    announcement = f"may i have your attention please! Train number {train_no_sort}  from {from_station} via {via_stations} to {to_station} {train_name} is on time and arrving on platform number {platform_number}"

    speak(announcement)

arriving_call()
