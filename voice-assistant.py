import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit as kit
import datetime
import os

# Initialize the voice engine
engine = pyttsx3.init()

# Function to speak the assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}\n")
    except Exception as e:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
        return None
    return command.lower()

# Function to execute commands
def execute_command(command):
    if 'hello' in command:
        speak("Hello, how can I assist you today?")
    
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"The current time is {current_time}")
    
    elif 'play' in command and 'music' in command:
        speak("Playing music for you.")
        kit.playonyt("music")
    
    elif 'wikipedia' in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    
    elif 'open' in command:
        speak("Opening website...")
        website = command.replace("open", "").strip()
        os.system(f"start {website}")
    
    elif 'stop' in command:
        speak("Goodbye!")
        exit()
    
    else:
        speak("I'm sorry, I don't know how to do that.")

# Main function to start the voice assistant
def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
