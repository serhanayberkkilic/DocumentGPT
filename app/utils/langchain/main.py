from langchain.llms import OpenAI
from app.core.config import openaisettings


class LangChain:

    def __init__(self):
        self.api_key = openaisettings.key
        self.openai = OpenAI(openai_api_key=self.api_key)

    def QuestionAnswer(self, question):
        response = self.openai.predict(question)
        return response