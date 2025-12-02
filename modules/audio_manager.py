from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
# Configuración de audio y modelo
samplerate = 16000
model = Model("vosk-model-small-es-0.42")
recognizer = KaldiRecognizer(model, samplerate)

def escuchar():
   """Graba 5 segundos de audio y devuelve el texto reconocido."""
   audio = sd.rec(int(5 * samplerate), samplerate=samplerate,
                  channels=1, dtype='int16')
   sd.wait()
   if recognizer.AcceptWaveform(audio.tobytes()):
     result = json.loads(recognizer.Result())
     return result.get("text", "")
   else:
     return ""
