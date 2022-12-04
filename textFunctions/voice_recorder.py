# voice recorder in python
import pyaudio
import wave

def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    print("recording...")
    
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")


    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    
    return WAVE_OUTPUT_FILENAME

def play_audio(filename):
    CHUNK = 1024

    wf = wave.open(filename, 'rb')

    p = pyaudio.PyAudio()

    # open stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

    print("Playing recorded audio")

    # read data
    data = wf.readframes(CHUNK)

    # play stream
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
        
    print("Finished playing recorded audio")

    # stop stream
    stream.stop_stream()
    stream.close()
    
    # close PyAudio
    p.terminate()
    
if __name__ == "__main__":
    filename = record_audio()
    # play_audio(filename)
