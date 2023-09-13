from app.core.config import openaisettings
import openai

class ChatCompletionClass:

    def __init__(self):
        openai.api_type = openaisettings.api_type
        openai.api_base = openaisettings.api_base
        openai.api_version = openaisettings.api_version
        openai.api_key = openaisettings.api_key


    def QuestionAnswer(self, question,datas):

        promt = datas+"\n\nQ: "+question+"\nA:"
        response = openai.Completion.create(
            engine="GTP3-5",
            prompt=promt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"])

        response = response["choices"][0]["text"]
        return response