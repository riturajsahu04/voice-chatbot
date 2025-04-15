from google.cloud import dialogflow_v2 as dialogflow

class DialogflowService:
    def __init__(self, project_id, credentials):
        self.project_id = project_id
        self.session_client = dialogflow.SessionsClient(credentials=credentials)

    def detect_intent(self, session_id, text, language_code='en'):
        session = self.session_client.session_path(self.project_id, session_id)
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = self.session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response

    def send_response(self, response):
        return response.query_result.fulfillment_text