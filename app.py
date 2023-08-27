# Import necessary libraries and modules
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import openai
import matplotlib
from pandasai import SmartDataframe

matplotlib.use('TkAgg')

# Get API key
#OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

OPENAI_API_KEY= "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"
# Set OpenAI API key
openai.api_key = "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"

llm = OpenAI(api_token=OPENAI_API_KEY)

# Set page configuration and title ofor Streamlit
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
    """pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    print(type(result))
    print(result)
    return result"""
    result=df.chat(prompt)
    #print(result)
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
            data = SmartDataframe(data, config={"llm": llm})

            st.dataframe(data)

# ... [Your previous code]

        with col2:
            st.markdown("## 🤖 Chat with DataSage")
            input_text = st.text_area("What would you like to know?", height=100)
            if st.button("Ask DataSage"):
                if input_text:  # Check if the prompt is not empty
                    st.info(f"Your Query: *{input_text}*")
                    with st.spinner("Generating response..."):  # Add a spinner
                        
                        result = chat_with_csv(data, input_text)
                                                # Check the type of the result and display accordingly
                        if isinstance(result, pd.DataFrame):
                            st.dataframe(result)
                        elif isinstance(result, list):
                            st.success(' '.join(map(str, result)))
                        else:
                            st.success(result)


                else:
                    st.warning("Please enter a prompt.")  # Warning message for empty prompt

        # ... [Rest of your code]

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
