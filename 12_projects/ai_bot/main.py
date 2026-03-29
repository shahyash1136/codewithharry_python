from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

messages = []

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key
)


def completion(message):
    global messages
    messages.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )
    print(completion)
    message = {"role": "assistant", "content": completion.choices.message.content}
    messages.append(message)
    print(f"Jarvis: {message["content"]}")


if __name__ == "__main__":
    print(f"Jarvis: Hi I am Jarvis, How may I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)
