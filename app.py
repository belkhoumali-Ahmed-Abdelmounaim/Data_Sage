# Import necessary libraries and modules
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import openai

# Get API key
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Set page configuration and title for Streamlit
st.set_page_config(page_title="DataSage", page_icon="🔮", layout="wide")

# Add header with title and description
st.markdown(
    '<div style="text-align:center;">'
    '<p style="font-size:40px;font-weight:bold;color:#5C4DB1;">🔮 DataSage </p>'
    '<p style="font-size:18px;color:#888888;">Unravel the mysteries of your CSV data with the power of AI. '
    'Simply upload, ask, and let DataSage provide insights.</p>'
    '</div>',
    unsafe_allow_html=True
)

def chat_with_csv(df, prompt):
    llm = OpenAI(api_token=OPENAI_API_KEY)
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    return result

# Create a container for the file uploader and chat
container = st.container()

with container:
    st.markdown('<div style="border: 2px solid #E0E0E0; border-radius: 10px; padding: 20px;">', unsafe_allow_html=True)
    input_csv = st.file_uploader("📤 Upload your CSV file", type=['csv'])

    if input_csv is not None:
        col1, col2 = st.columns([1, 1])

        with col1:
            st.info("📄 Preview of Uploaded CSV")
            data = pd.read_csv(input_csv)
            st.dataframe(data)

        with col2:
            st.markdown("## 🤖 Chat with DataSage")
            input_text = st.text_area("What would you like to know?", height=100)
            if st.button("Ask DataSage"):
                st.info(f"Your Query: *{input_text}*")
                result = chat_with_csv(data, input_text)
                st.success(result)
    st.markdown('</div>', unsafe_allow_html=True)

# Hide Streamlit header, footer, and menu
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

# Apply CSS code to hide header, footer, and menu
st.markdown(hide_st_style, unsafe_allow_html=True)
