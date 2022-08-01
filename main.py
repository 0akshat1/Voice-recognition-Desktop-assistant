import pyttsx3
import speech_recognition as sr
import wikipedia
import random


engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    speak("good morning everyone ")
    speak("i am professor please tell me how may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300  #for silent room 100 to 300 and for noisy room 400 to 3500
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en in')
        print(f"user said: {query}\n")


    except Exception as e:

        print("say that again please")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True:
      query = takecommand().lower()

      if 'wikipedia' in query:
          speak('searching wikipedia')
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=2)
          speak("according to wikipedia")
          print(results)
          speak(results)

      elif 'random' in query:
          speak('giving random slots')
          query = slot = [[1, 4], [2, 3]]
          results = slot[random.randrange(0, 2)]
          results = slot[random.randrange(0, 2)]
          speak("according to me for tdm slots are")
          print(results)
          speak(results)


      elif 'quit' in query:
          speak("okay professor signing out")
          exit()







