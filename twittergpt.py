import os
import openai

openai.api_key = "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"
messages = []

for i in range(2):
    user_content = input("User : ")
    messages.append({"role": "user", "content": f"{user_content}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": f"{assistant_content}"})
    print(f"GPT : {assistant_content}")
