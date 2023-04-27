import os
import openai

openai.api_key = " "
messages = []

for i in range(1):
    user_content = "(그냥 오징어게임이나 극장에 상영해주세요…..)라는 문장의 감정을 한단어로 얘기해줘"
    messages.append({"role": "user", "content": f"{user_content}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": f"{assistant_content}"})
    print(f"GPT : {assistant_content}")
