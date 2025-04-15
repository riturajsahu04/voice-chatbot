def load_env_variables():
    """Load environment variables from the .env file."""
    from dotenv import load_dotenv
    import os

    load_dotenv()

def format_response(response):
    """Format the response from the chatbot."""
    return response.strip() if response else "I'm sorry, I didn't understand that."