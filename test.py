import streamlit as st
import requests
import json
import urllib

# Azure AD Configuration
CLIENT_ID = "f4e9cfb1-5e45-4383-94be-ab9d078cef68"  # Update if needed
AUTHORITY = "https://login.microsoftonline.com/consumers"  # Update if needed
CLIENT_SECRET = "Qms8Q~WRiwqIrP2Z67O81dBEmS~SuElVFkYy6aSz"  # Update if needed
REDIRECT_PATH = "/"

# Generate Azure AD login URL
def generate_login_url():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": f"http://localhost:8501",
        "scope": "User.Read",
    }
    login_url = f"{AUTHORITY}/oauth2/v2.0/authorize?{urllib.parse.urlencode(params)}"
    return login_url

# Fetch token from Azure AD
def fetch_token(code):
    token_url = f"{AUTHORITY}/oauth2/v2.0/token"
    token_data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "User.Read",
        "code": code,
        "redirect_uri": f"http://localhost:8501",
    }
    token_r = requests.post(token_url, data=token_data)
    token = token_r.json()
    return token

# Login page
def login_page():
    st.title("Azure AD Authentication with Streamlit")
    
    # Check if user is already authenticated
    session_state = st.session_state
    if "auth_token" not in session_state:
        session_state["auth_token"] = None

    if session_state["auth_token"]:
        st.success("You are authenticated. Go to the next page.")
    else:
        st.warning("You are not authenticated.")
        login_url = generate_login_url()
        st.markdown(f"[Click here to login]({login_url})")

    if st.experimental_get_query_params().get("code"):
        code = st.experimental_get_query_params()["code"][0]
        token = fetch_token(code)
        session_state["auth_token"] = token["access_token"]
        st.experimental_set_query_params(code=None)  # Clear the query param

# Success page
def success_page():
    st.title("Successfully Logged In")
    st.markdown("You have successfully logged in to the application!")
    st.image("https://image.shutterstock.com/image-photo/beautiful-sunrise-over-typical-suburban-260nw-434541056.jpg")

# Main Streamlit App
def main():
    # Initialize session_state
    session_state = st.session_state
    if "auth_token" not in session_state:
        session_state["auth_token"] = None
    
    # Page routing
    page_options = ["Login Page", "Success Page"]
    selected_page = st.sidebar.selectbox("Navigation", page_options)
    
    if selected_page == "Login Page":
        login_page()
    elif selected_page == "Success Page":
        if session_state["auth_token"]:
            success_page()
        else:
            st.warning("You need to authenticate first.")
            st.experimental_reroute("/")

if __name__ == "__main__":
    main()
