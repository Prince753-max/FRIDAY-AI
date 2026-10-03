import numpy as np
import sounddevice as sd
from openwakeword.model import Model

SAMPLE_RATE = 16000
CHUNK = 1280  # 80ms at 16kHz


def listen_for_wake_word(keyword="hey_jarvis"):
    """Blocks until the wake word is heard, then returns."""
    model = Model(wakeword_models=[keyword], inference_framework="onnx")
    print(f"Listening for wake word '{keyword}'...")
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="int16") as stream:
        while True:
            audio, _ = stream.read(CHUNK)
            audio = audio.flatten().astype(np.int16)
            prediction = model.predict(audio)
            for mdl, score in prediction.items():
                if score > 0.2:
                    print("Wake word detected!")
                    return