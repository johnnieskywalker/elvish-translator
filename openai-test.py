from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
language = input("Enter the language to translate from: ")
text = input("Enter the text to translate: ")

try:
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Translate the following {text} from {language} to Elfish from LOTR"}
        ]
    )
    print(completion.choices[0].message.content)
except AttributeError:
    print("The method you are trying to use is not available. Check the latest API documentation.")