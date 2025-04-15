from services.speech_to_text import SpeechToTextService
from services.dialogflow import DialogflowService
from services.text_to_speech import TextToSpeechService
from config.settings import Settings
from utils.helpers import load_env_variables
from google.oauth2.service_account import Credentials
import os

def main():
    # Load environment variables (if needed for dynamic overrides)
    load_env_variables()

    # Load credentials and project ID from settings
    credentials = Credentials.from_service_account_file(Settings.GOOGLE_APPLICATION_CREDENTIALS)
    project_id = Settings.PROJECT_ID

    # Initialize services
    speech_service = SpeechToTextService()
    dialogflow_service = DialogflowService(project_id=project_id, credentials=credentials)
    text_to_speech_service = TextToSpeechService()

    # Main loop for user interaction
    print("Voice Chatbot is running. Speak to interact...")
    switch = True
    while switch:
        # Specify the audio file path
        audio_file_path = os.path.join(os.getcwd(), "voice-chatbot", "audio", "Recording.wav")  # Replace with the path to your audio file

        # Capture audio and transcribe to text
        transcripts = speech_service.transcribe_audio(audio_file_path)
        if not transcripts:
            print("No speech detected. Please try again.")
            continue

        # Use the first transcript as the user input
        user_input = transcripts[0]
        print(f"User: {user_input}")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chatbot.")
            break
        
        # Process user input with Dialogflow
        response = dialogflow_service.detect_intent(session_id="12345", text=user_input)
        response_text = response.query_result.fulfillment_text  # Extract the text response from Dialogflow
        print(f"Bot: {response_text}")
        
        # Convert response text to speech and save the audio
        audio_content = text_to_speech_service.synthesize_speech(response_text)
        output_audio_path = os.path.join(os.getcwd(), "voice-chatbot", "audio", "Response.wav")
        with open(output_audio_path, "wb") as audio_file:
            audio_file.write(audio_content)
        print(f"Bot response audio saved to {output_audio_path}")
        switch = False

if __name__ == "__main__":
    main()