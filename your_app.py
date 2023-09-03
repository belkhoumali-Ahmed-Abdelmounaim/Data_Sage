import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import openai
import os
import matplotlib.pyplot as plt
import matplotlib

import sqlite3
import hashlib


conn = sqlite3.connect('user_data.db')
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')

def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username, password) VALUES (?, ?)', (username, password))
    conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username=? AND password=?', (username, password))
    data = c.fetchall()
    return data


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


matplotlib.use('Agg')

# Streamlit Configuration
st.set_page_config(page_title="DataSage", page_icon="🔮", layout="wide")

# OpenAI Configuration
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_user_state():
    if 'user_state' not in st.session_state:
        st.session_state['user_state'] = {'username': None, 'is_logged_in': False}
    return st.session_state['user_state']


def chat_with_csv(df, prompt):
    llm = OpenAI(api_token=OPENAI_API_KEY)
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    return result

# Main function to control the app
def main():
    user_state = get_user_state()

    st.sidebar.title("Menu")
    menu = ["Home", "SignIn", "SignUp"]
    choice = st.sidebar.selectbox("Choose an option", menu)

    if choice == "Home":
        if user_state['is_logged_in']: 
            st.subheader(f"Welcome {user_state['username']}!")
            st.markdown(
            '<div style="text-align:center;">'
            '<p style="font-size:40px;font-weight:bold;color:#5C4DB1;">🔮 DataSage </p>'
            '<p style="font-size:18px;color:#888888;">Unravel the mysteries of your CSV data with the power of AI. '
            'Simply upload, ask, and let DataSage provide insights.</p>'
            '</div>',
            unsafe_allow_html=True
            )
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
                            if input_text:
                                st.info(f"Your Query: *{input_text}*")
                                with st.spinner("Generating response..."):
                                    result = chat_with_csv(data, input_text)
                                    if isinstance(result, pd.DataFrame):
                                        st.dataframe(result)
                                    else:
                                        st.success(result)
                            else:
                                st.warning("Please enter a prompt.")
        else : 
            st.warning("You need to log in to access this page.")
            st.info("Go to SignIn to log in.")

    elif choice == "SignIn":
        st.subheader("Sign In to DataSage")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')

        create_usertable()
        hashed_pswd = make_hashes(password)

        if st.sidebar.checkbox("Sign In"):
            result = login_user(username, check_hashes(password, hashed_pswd))
            if result:
                user_state['username'] = username
                user_state['is_logged_in'] = True
                st.success(f"Logged In as {username}")
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Sign Up for DataSage")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Sign Up"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You've successfully signed up for DataSage!")
            st.info("Go to SignIn to login")

if __name__ == '__main__':
    main()
