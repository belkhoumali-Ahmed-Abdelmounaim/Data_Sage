import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize Firebase
cred = credentials.Certificate("src/secrets2.json")
firebase_admin.initialize_app(cred)

def app():
    st.title('DataSage User Portal ')

    # Apply styles
    st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(90deg, #212E53 30%, #4A919E 90%);
            background-attachment: fixed;
            background-size: cover;
            min-height: 100vh;
        }
        .stTextInput > div > div > input {
            color: black !important;
        }
        h1, h2, h3, h4, h5, h6, label, body, span, p, a {
            color: white !important;
        }
        .icon {
            font-size: 1.5em;
            vertical-align: middle;
            margin-right: 10px;
            color: white;
        }
        div.row-widget.stRadio > div {
            flex-direction: row;
            align-items: stretch;
        }
        div.row-widget.stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] {
            background-color: #9AC5F4;
            padding-right: 10px;
            padding-left: 4px;
            padding-bottom: 3px;
            margin: 4px;
            color: black !important;
        }
        }
        </style>
    """, unsafe_allow_html=True)

    
    # User icon at the top center
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <i class="fas fa-user-circle" style="font-size: 4em; color: #f1c40f;"></i>
        </div>
    """, unsafe_allow_html=True)

    # Initialize session state variables
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False

    # Functions to handle login and logout
    def f(): 
        try:
            user = auth.get_user_by_email(email)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signedout = True
            st.session_state.signout = True    
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''

    # User authentication fields with icons
    email = st.text_input('Email Address', placeholder="Email Address")
    password = st.text_input('Password', type='password', placeholder="**********")

    # Account login and creation
    if not st.session_state["signedout"]:
        choice = st.radio('Choose an option:', ['Login', 'Sign up'])

        if choice == 'Sign up':
            username = st.text_input("Enter your unique username")
            
            if st.button('Create my account'):
                user = auth.create_user(email=email, password=password, uid=username)
                st.success('Account created successfully!')
                st.markdown('Please login using your email and password')
                st.balloons()
        else:
            st.button('Login', on_click=f)
    
    # Account dashboard
    if st.session_state.signout:
        st.markdown(f'<div style="color: white;">Name: {st.session_state.username}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color: white;">Email ID: {st.session_state.useremail}</div>', unsafe_allow_html=True)
        st.button('Sign out', on_click=t)

