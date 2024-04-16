import streamlit as st
from openai import OpenAI

# Set page title and background color
st.title("🐍 Python Code Debugger")
st.markdown(
    """
    <style>
        .stApp {
            background-color: #4A646C;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Read the private key and set up a client
with open("Keys/.openai_demo_key.txt") as f:
    key = f.read()
client = OpenAI(api_key=key)

# Create an input box for code
label = "Enter your Python code"
prompt = st.text_area(label)

# If the button is clicked, generate the output
if st.button("Generate"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {'role': 'system', 'content': """
                You are a helpful AI assistant. Given a Python code, show where the errors or bugs are present,
                and also debug and give the correct code.
                """},
            {'role': 'user', 'content': prompt}
        ]
    )
    st.write(response.choices[0].message.content)
