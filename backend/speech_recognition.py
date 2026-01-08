import vosk
import sounddevice as sd
import json

model = vosk.Model("models/vosk-model")
recognizer = vosk.KaldiRecognizer(model, 16000)

def speech_to_text():
    print("🎙 Listening... Speak now")

    def callback(indata, frames, time, status):
        if recognizer.AcceptWaveform(indata):
            pass

    with sd.RawInputStream(samplerate=16000,
                           blocksize=8000,
                           dtype='int16',
                           channels=1,
                           callback=callback):
        while True:
            result = recognizer.Result()
            text = json.loads(result).get("text", "")
            if text:
                print("Recognized:", text)
                return text
