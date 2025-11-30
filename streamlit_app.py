import streamlit as st
import time
import requests
from bs4 import BeautifulSoup
import random

# Setup the page
st.set_page_config(
    page_title="AIU School Assistant",
    page_icon="🏫",
    layout="wide"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("🏫 African International University Assistant")
    st.write("I can help with:")
    st.write("• Courses & Programs")
    st.write("• Admissions Process") 
    st.write("• Campus Facilities")
    st.write("• Sports & Athletics 🏀")
    st.write("• Clubs & Activities 🎭")
    st.write("• Student Services")
    st.write("• Financial Information")
    st.write("• Internet Search 🔍")
    
    st.divider()
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Main page
st.title("🎓 African International University Assistant")
st.write("Welcome to AIU! Ask me anything about our university - courses, sports, clubs, admissions, and more!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def search_internet(query):
    """Search for information online about AIU"""
    try:
        # Provides helpful links instead of unreliable web scraping
        return (
            "🔍 **Online Search Results:**\n\n"
            "For the most current and accurate information about African International University, "
            "please visit:\n\n"
            "• **Official Website:** www.aiu.ac.ke\n"
            "• **Admissions Email:** admissions@aiu.edu\n"
            "• **Phone:** +254 796 352 397 / +254 748 759 496\n"
            "• **Admissions Hotline:** +254 725 841 885\n\n"
            "💡 *Tip: Search 'African International University Kenya' on Google for the latest news and updates!*"
        )
    except Exception as e:
        return "I couldn't process the search right now. Please visit the official AIU website directly at www.aiu.ac.ke"

def get_school_response(user_input):
    user_input = user_input.lower()
    
    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 I'm your AIU (African International University) assistants