import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import webbrowser

# This is text to speech
def text_to_speech_gtts(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("robot_brain.mp3")
    os.system("start robot_brain.mp3")

# This is speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("You: ", end='')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='vi-VN')
            print(text)  # Text user says to the robot
            # Train models assistant
            if text == "":
                robot_brain = "What do you say to me."
                text_to_speech_gtts(robot_brain)
                print("Robot brain: ", robot_brain)  # Text robot says to human
            elif "hello" in text or "hi" in text:
                robot_brain = "Hello, what can I help you ?"
                text_to_speech_gtts(robot_brain)
                print("Robot brain: ", robot_brain)  # Text robot says to human
            elif "goodbye" in text:
                robot_brain = "Farewell."
                text_to_speech_gtts(robot_brain)
                print("Robot brain: ", robot_brain)  # Text robot says to human
                break
            elif "hour" in text or "time" in text:
                time_now = datetime.now()
                robot_brain = f"{time_now.hour}:{time_now.minute}:{time_now.second}"
                text_to_speech_gtts(robot_brain)
                print("Robot brain: ", robot_brain)
            elif "youtube" in text:
                youtube_url = "https://www.youtube.com"
                webbrowser.open(youtube_url)
                robot_brain = " oki, i will open youtube"
                text_to_speech_gtts(robot_brain)
                print("Robot brain: ", robot_brain)
            else :
                robot_brain = "sorry, i didn't hear you, can you say it again."
                text_to_speech_gtts(robot_brain)
                print("Robot brain: ", robot_brain)  # Text robot says to human

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


# This is main
if __name__ == "__main__":
    speech_to_text()
