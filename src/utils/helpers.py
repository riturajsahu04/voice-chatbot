import pyaudio
import wave
from dotenv import load_dotenv
import os

def load_env_variables():
    """Load environment variables from the .env file."""
    load_dotenv()

def format_response(response):
    """Format the response from the chatbot."""
    return response.strip() if response else "I'm sorry, I didn't understand that."

def record_audio(output_file, duration=5):
    """Record audio from the microphone and save it to a file."""
    chunk = 1024  # Record in chunks of 1024 samples
    format = pyaudio.paInt16  # 16-bit resolution
    channels = 1  # Mono audio
    rate = 8000  # 8kHz sample rate
    p = pyaudio.PyAudio()

    print("Recording...")
    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording complete.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a file
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

def play_audio(file_path):
    """Play the audio file through the speakers."""
    chunk = 1024  # Define chunk size
    wf = wave.open(file_path, 'rb')
    p = pyaudio.PyAudio()

    # Open a stream to play the audio
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Read and play the audio in chunks
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()