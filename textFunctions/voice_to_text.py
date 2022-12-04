import librosa
import numpy as np
import os
import soundfile as sf
import time
import torch
from IPython.display import Audio
from scipy.io.wavfile import read, write
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

print("Loading the model... please wait")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")


def read_audio_file(path):
    # Audio(path)
    data = read(path)
    # data[0] is the sampling rate of the audio file
    # data[1] is the audio file itself
    print("Sampling rate: ", data[0], "Hz")
    audio_file, _ = librosa.load(path, sr=16000)
    return audio_file, data[0]

def speech_to_text(audio_file, sampling_rate):
    # Convert the audio file to a tensor
    input_values = processor(audio_file, sampling_rate=sampling_rate, return_tensors="pt").input_values
    # Get the logits from the model
    logits = model(input_values).logits
    # Take the argmax of the logits to get the predicted ID for each input frame
    predicted_ids = torch.argmax(logits, dim=-1)
    # Decode the audio input to get the text
    transcription = processor.batch_decode(predicted_ids)[0]
    return transcription

if __name__ == "__main__":
    os.system("rm -rf ./output.wav")
    os.system("python ./textFunctions/voice_recorder.py")
    time.sleep(1)
    audio_file, sampling_rate = read_audio_file("output.wav")
    transcription = speech_to_text(audio_file, 16000)
    print(transcription)