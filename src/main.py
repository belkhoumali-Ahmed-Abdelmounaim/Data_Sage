import streamlit as st

# Importing the modules representing different sections of your app
import home
import about
import account
import time
from streamlit_option_menu import option_menu
import warnings
warnings.simplefilter("ignore", UserWarning)


# Setting the page configuration with a custom title
st.set_page_config(page_title="DataSage")

class MultiApp:
    """A class to represent a Streamlit multi-app.

    This class is responsible for managing multiple Streamlit applications and rendering the selected app based on the user's selection from the sidebar option menu.

    Attributes:
        apps: A list to store the details (title and function) of individual apps.
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds an app to the multi-app list.

        Args:
            title (str): The title of the app.
            func (callable): A function that renders the app in the Streamlit interface.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

def run():
    """Displays the sidebar and runs the selected app."""
    # Creating the sidebar with option menu for selecting the desired section (home, account, about)
    with st.sidebar:        
        app = option_menu(
            menu_title='Pondering ',
            options=['home','account','about'],
            icons=['house-fill','person-circle','info-circle-fill'],
            menu_icon='chat-text-fill',
            default_index=1,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"}, 
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )

    # Display the selected app based on the user's choice from the sidebar option menu
    if app == "home":
        if 'username' in st.session_state and st.session_state.username:
            home.app()
        else:
            with st.spinner("Redirecting..."):
                time.sleep(1)
            st.warning("You need to log in first to access this page.")
            account.app()
    elif app == "account":
        account.app()
    elif app == 'about':
        about.app()

# Call the run function to initiate the multi-app
run()
