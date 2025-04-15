from google.cloud import speech_v1p1beta1 as speech

class SpeechToTextService:
    def __init__(self):
        self.client = self.configure_client()

    def configure_client(self):
        client = speech.SpeechClient()
        return client

    def transcribe_audio(self, audio_file_path):
        with open(audio_file_path, 'rb') as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,  # Updated to AAC-M4A encoding
            sample_rate_hertz=8000,  # Updated to match your microphone's sample rate
            language_code='en-IN',  # Updated to Indian English
            enable_automatic_punctuation=True,  # Enable automatic punctuation
            model='default',  # Use default model
            use_enhanced=True,  # Use enhanced model for better accuracy
            audio_channel_count=1,  # Mono audio
            enable_word_time_offsets=True,  # Enable word time offsets
            enable_speaker_diarization=True,  # Enable speaker diarization
            diarization_speaker_count=1,  # Number of speakers in the audio
            enable_word_confidence=True,  # Enable word confidence scores
            max_alternatives=1,  # Return only the best alternative
        )
        
        response = self.client.recognize(config=config, audio=audio)

        transcripts = []
        for result in response.results:
            transcripts.append(result.alternatives[0].transcript)

        return transcripts