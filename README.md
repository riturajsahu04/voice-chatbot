# Voice Chatbot

This project is a voice chatbot that utilizes Google Cloud Platform's Speech-to-Text, Dialogflow, and Text-to-Speech functionalities to provide an interactive voice-based user experience.

## Project Structure

```
voice-chatbot
├── src
│   ├── main.py                # Entry point of the application
│   ├── services               # Contains service classes for speech and text processing
│   │   ├── speech_to_text.py  # Speech-to-Text service
│   │   ├── dialogflow.py       # Dialogflow service for intent processing
│   │   └── text_to_speech.py   # Text-to-Speech service
│   ├── config                 # Configuration settings
│   │   └── settings.py        # API keys and project IDs
│   └── utils                  # Utility functions
│       └── helpers.py         # Helper functions for various tasks
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables
├── .gitignore                 # Files to ignore in Git
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd voice-chatbot
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create a `.env` file in the root directory and add your Google Cloud API keys and other configuration settings.

5. **Run the application:**
   ```
   python src/main.py
   ```

## Usage Guidelines

- The chatbot listens for user input through the microphone, processes the speech to detect intents using Dialogflow, and responds with synthesized speech.
- Ensure that your Google Cloud services are properly set up and that you have the necessary permissions to access the Speech-to-Text and Text-to-Speech APIs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.