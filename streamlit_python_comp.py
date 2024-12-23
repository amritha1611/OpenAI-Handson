from openai import OpenAI 
import streamlit as st

f = open('keys/.openai_api_key.txt')
OPENAI_API_KEY = f.read()

client = OpenAI(api_key=OPENAI_API_KEY)

def python_compiler(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """I want you to act as a Python Compiler. I will type a python code and you will reply with what the Python Console should show. I want you to only reply with the terminal output inside a unique code block. Do not write the explanations, do not type any commands unless I instruct you to do so. When I need to tell you something in English, I will do so by putting text inside triple hashes ### like this ###. Let's start with the first Python Code."""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

prompt = st.text_area("Enter you Python Program")

if st.button("Compile"):
    st.write(python_compiler(prompt))
