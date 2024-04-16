import streamlit as st
from openai import OpenAI

# Function to read API key from file
def read_api_key(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()

# Function to call OpenAI API for code review
def analyze_code(code, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You're a Python code debugger AI assistant. Your task is to identify 
                and fix bugs in Python code. Provide explanations for the bugs and suggest corrected code. 
                Format: Bugs: [Description of errors], Explanation, Fixed code: [Corrected code]."""
            },
            {"role": "user", "content": code}
        ],
        temperature=0.5  # Adjusted temperature for more focused responses
    )
    return response.choices[0].message.content.strip()

# Streamlit App
def main():
    st.title("Your Python Code AI Companion")
    st.write("Welcome to Python Code AI, your friendly Python code reviewer!")

    # Input interface
    code = st.text_area("Paste your Python code here:")

    if st.button("Review My Code"):
        if code.strip() == "":
            st.error("Please enter some Python code.")
        else:
            # Read API key from file
            api_key = read_api_key(".openaikey.txt")
            st.write("Analyzing your code...")
            reviewed_code = analyze_code(code, api_key)
            st.subheader("Reviewed Code:")
            st.code(reviewed_code, language="python")

if __name__ == "__main__":
    main()
