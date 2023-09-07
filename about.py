import streamlit as st

def app(): 
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background: linear-gradient(45deg, #fffbf0, #ffe6d9);
    }
    .icon {
        font-size: 1.5em;
        vertical-align: middle;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)
    st.title("About DataSage 🌐")

    st.write(
        """
        Welcome to DataSage, your go-to platform for unraveling the deep secrets lying in your CSV data with the power of Artificial Intelligence. Here is everything you need to know about DataSage:
        """
    )

    # Section: What is DataSage
    st.header("🤔 What is DataSage?")
    st.write(
        """
        DataSage is an AI-driven tool designed to help users analyze and extract insights from their CSV data files effortlessly. Just upload your CSV file, and start a chat with DataSage. Ask questions, get infos, and explore your data like never before!
        """
    )

    # Section: How it Works
    st.header("🛠 How it Works")
    st.write(
        """
        **Step 1:** Upload your CSV file using the file uploader on the Home page.
        
        **Step 2:** Preview the uploaded data and make sure it's the right dataset.
        
        **Step 3:** Enter your queries or questions in the chat section. You can ask anything related to your data.
        
        **Step 4:** Hit "Ask DataSage" and voila! Get detailed insights and answers based on your data.

        It's that simple and intuitive!
        """
    )

    # Section: Features
    st.header("🌟 Features")
    st.write(
        """
        - **Data Preview:** Preview your uploaded data before analyzing it.
        - **AI-Powered Chat:** An intuitive chat interface powered by OpenAI to answer your data-related queries.
        - **Display plots:** You can display any plot of any column (or combination of columns) with a simple prompt with any color you want and any stylings.
        - **Secure Authentication:** A secure authentication system to protect your data and preferences.
        """
    )

    # Section: Contact Us
    st.header("📬 Contact Us")
    st.write(
        """
        Have questions, suggestions, or feedback? We would love to hear from you. Reach out to us at [datasage@example.com](mailto:datasage@example.com).
        """
    )

    # Section: Follow Us
    st.header("🌐 Follow Us")
    st.write(
        """
        Stay updated with the latest features and updates. Follow us on our social media platforms:

        - [GitHub](https://github.com/)
        - [Twitter](https://twitter.com/)
        - [LinkedIn](https://linkedin.com/)
        """
    )

    # Encourage users to start using DataSage
    st.write(
        """
        Ready to explore your data? [Start using DataSage now!](#)
        """
    )

    # Footer
    st.write(
        """
        ---
        © 2023 DataSage | All rights reserved
        """
    )
