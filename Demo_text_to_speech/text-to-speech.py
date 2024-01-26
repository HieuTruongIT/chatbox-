from gtts import gTTS
import os

def text_to_speech_gtts(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("robot_brain.mp3")
    os.system("start robot_brain.mp3")

if __name__ == "__main__":
    text = input("You: ")
    text_to_speech_gtts(text)
