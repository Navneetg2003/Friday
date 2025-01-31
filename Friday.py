import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import random
import threading
import pyaudio
import tkinter as tk
from tkinter import messagebox

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    def task():
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            speak(" Good morning User!")
        elif 12 <= hour < 18:
            speak("Good afternoon!")
        else:
            speak("Good evening!")
        speak("I am Friday. Please tell me how can I help you!")
    threading.Thread(target=task).start()

def VoiceCommand():
    def task():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Listening...")
            print("Listening...")
            try:
                audio = r.listen(source)
                query = r.recognize_google(audio)
                print(f"User said: {query}")
                processCommand(query)
            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand you.")
            except sr.RequestError:
                speak("Network error. Please check your connection.")
    threading.Thread(target=task).start()
def TextCommand():
    query = input_box.get()
    processCommand(query)
def quit():
    speak(" Thank you for using me")
    root.quit()
def processCommand(query):
    def task():
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            messagebox.showinfo("Wikipedia Result", results)
            speak(results)
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            messagebox.showinfo("Current Time", strTime)
        else:
            speak("I'm sorry, I didn't understand. Please try again.")
    threading.Thread(target=task).start()
def start_wake_detection():
    
# GUI Setup
root = tk.Tk()
root.title("Friday - AI Assistant")
root.geometry("400x300")

label =tk.Label(root,text="Hello, I am Friday - your new AI Assistant!")
label.pack(pady=10)

label = tk.Label(root, text="Type your command below:")
label.pack(pady=10)

input_box = tk.Entry(root, width=40)
input_box.pack(pady=10)

Voice_button=tk.Button(root,text="Voice Command",command=VoiceCommand)
Voice_button.pack(pady=20)

submit_button = tk.Button(root, text="Submit", command=TextCommand)
submit_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit)
quit_button.pack(pady=10)

wishMe()
start_wake_detection()
root.mainloop()