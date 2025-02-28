import pyttsx3
import speech_recognition as sr
import openai
import os
from dotenv import load_dotenv
import time

# Load API key from .env file (or set it as an environment variable)
load_dotenv()
OPENAI_API_KEY = ""

# Initialize OpenAI API
client = openai.OpenAI(api_key=OPENAI_API_KEY)  # ✅ Correct API initialization

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

def speak(text):
    """Convert text to speech"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for user input via microphone"""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=10)
                command = recognizer.recognize_google(audio).lower()
                print(f"User said: {command}")
                return command
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Can you repeat?")
            except sr.RequestError:
                speak("Speech service is unavailable at the moment.")
    except OSError:
        print("❌ Error: No microphone detected!")
        return ""
    
    return ""

def chat_with_openai(prompt):
    """Send user input to OpenAI API and return response"""
    try:
        response = client.chat.completions.create(  # ✅ Correct API method
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content  # ✅ Correct response extraction

    except openai.OpenAIError as e:  # ✅ Correct exception handling
        print(f"❌ OpenAI API Error: {e}")
        return "Sorry, I couldn't process your request."

def assistant():
    """Main voice assistant loop"""
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye! Have a productive day!")
                break
            else:
                response = chat_with_openai(command)
                speak(response)

if __name__ == "__main__":
    assistant()
