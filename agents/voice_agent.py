# -----------------------------
import pyttsx3
import whisper

model = whisper.load_model("base")
engine = pyttsx3.init()

def transcribe(audio_path):
    return model.transcribe(audio_path)['text']

def speak(text):
    engine.say(text)
    engine.runAndWait()
