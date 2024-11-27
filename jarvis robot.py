import speech_recognition as sr
import pyttsx3
import os
import platform
import sys

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Set the speech rate here

def mic_input():
    """Takes input from the microphone and returns it as a string"""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=30, phrase_time_limit=20)
        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in').lower()
            print(f"User said: {command}\n")
            return command
        except sr.UnknownValueError:
            print("I didn't catch that. Say that again please...")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
    except Exception as ex:
        print(f"Microphone input error: {ex}")
        return None

def tts(text):
    """Text to speech function"""
    try:
        engine.say(text)
        engine.runAndWait()
        return True
    except Exception as ex:
        print(f"Error in TTS: {ex}")
        return False

def greet_user():
    """Greets the user"""
    tts("RAM RAM, SIDDHU bhai ,I'm Chitti the Robot. Speed 1 terahertz, memory 1 zigabyte.. How can I assist you today?")

def play_music(file_path):
    """Plays a music file using the appropriate method based on the OS"""
    try:
        if platform.system() == "Windows":
            os.system(f'start "" "{file_path}"')
        elif platform.system() == "Darwin":  # macOS
            os.system(f'open "{file_path}"')
        elif platform.system() == "Linux":
            os.system(f'xdg-open "{file_path}"')
        else:
            print("Unsupported OS for playing music.")
    except Exception as ex:
        print(f"Error playing music: {ex}")

def take_user_input():
    """Takes user input and processes it"""
    while True:
        command = mic_input()
        if command is None:
            continue  # Repeat the loop if the command wasn't understood
        if "by" in command:
            tts("Goodbye!")
            sys.exit()  # Exit the program
        if "launch" in command:
            # Launch an application
            tts("Launching application...")
            os.system("start chrome.exe")
        
        elif 'no' in command:
            os.system("start Avengers.py")

        elif "weather" in command:
            # Get weather information
            tts("Getting weather report...")
            weather, temperature, feels_like = get_weather_report("your_city")
            if weather and temperature and feels_like:
                tts(f"The current temperature is {temperature}, but it feels like {feels_like}")
                tts(f"Also, the weather report talks about {weather}")
            else:
                tts("Sorry, I couldn't fetch the weather information.")
        elif "play music" in command:
            # Specify the path to your music file here
            tts("okay i wll play music")
            music_file = "C:/Users/siddh/Downloads/WhatsApp Audio 2022-11-14 at 1.43.16 PM.mpeg"
            play_music(music_file)
        elif "khaegi" in command:
            tts("i wanna eat pizza!")
        else:
            tts("I didn't understand that. Please try again.")

def get_weather_report(city):
    """Stub function to get weather report"""
    # Implement actual weather API call here
    return "sunny", "25°C", "23°C"  # Example values

greet_user()
while True:
    take_user_input()
