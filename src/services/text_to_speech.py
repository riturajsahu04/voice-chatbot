from google.cloud import texttospeech

class TextToSpeechService:
    def __init__(self):
        self.client = self.configure_client()

    def configure_client(self):
        client = texttospeech.TextToSpeechClient()
        return client

    def synthesize_speech(self, text, language_code='en-IN'):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16  # Changed to LINEAR16 for WAV format
        )

        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        return response.audio_content