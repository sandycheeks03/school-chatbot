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
        # You can customize this search for your actual university website
        search_url = f"https://www.google.com/search?q=African+International+University+{query}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract some basic info (this is simplified)
        results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
        if results:
            return f"🔍 According to online sources: {results[0].get_text()[:200]}..."
        else:
            return "I found some online information but couldn't extract specific details. Please visit the official AIU website for accurate information."
            
    except Exception as e:
        return "I couldn't fetch online information right now. Please check the official AIU website directly."

def get_school_response(user_input):
    user_input = user_input.lower()
    
    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 I'm your AIU (African International University) assistant. How can I help you today?"
    
    # University info
    elif any(word in user_input for word in ["aiu", "african international", "university info", "about the school"]):
        return "🏫 **African International University (AIU)** is a prestigious institution committed to academic excellence and holistic student development. We offer diverse programs and vibrant campus life!"
    
    # Courses
    elif any(word in user_input for word in ["course", "program", "subject", "study", "major", "degree"]):
        return "📚 **Academic Programs at AIU:**\n•Diploma in AI and Cybersecurity & IT\n• Business Administration\n• Master of Arts in Church History\n• Certificate in Creative Animation and Robotics\n• Arts & Social Sciences\n• Education\n• Law School\n AIU offers a variety of Programs.Which field interests you?"
    
    # SPORTS - New Section
    elif any(word in user_input for word in ["sport", "athletic", "game", "team", "soccer", "basketball", "football", "volleyball", "tennis"]):
        return "🏀 **AIU Sports & Athletics:**\n• **Football/Soccer** (Men & Women teams)\n• **Basketball** (Competitive league)\n• **Volleyball** (Indoor)\n• **Table Tennis & Badminton**\n• **Track & Field**\n• **Martial Arts Club**\nWe have modern sports facilities and compete in inter-university tournaments!"
    
    # CLUBS & ACTIVITIES - New Section  
    elif any(word in user_input for word in ["club", "society", "activity", "extracurricular", "hobby", "organization"]):
        return "🎭 **Student Clubs & Activities at AIU:**\n• **Tech Club** - Coding, robotics, AI projects\n• **Business Society** - Entrepreneurship workshops\n• **Debate Club** - Public speaking & competitions\n• **Music & Arts Society** - Band, choir, theater\n• **Environmental Club** - Sustainability projects\n• **Cultural Associations** - International student groups\n• **Volunteer Corps** - Community service\n• **Photography Club** - Workshops & exhibitions\n• **Adventure Club** - Hiking, camping trips\nThere's something for everyone!"
    
    # Admissions
    elif any(word in user_input for word in ["admission", "apply", "enroll", "application", "requirement"]):
        return "📝 **AIU Admissions Process:**\n1. Submit online application\n2. Provide academic transcripts\n3. Write personal statement\n4. Letters of recommendation\n5. Entrance exam/interview\n6. Financial aid application\n\n**Deadlines:**\n• Fall Semester: August 15th\n• Spring Semester: January 10th"
    
    # Library
    elif any(word in user_input for word in ["library", "book", "study", "research"]):
        return "📚 **AIU Library:**\n• **Hours:** Mon-Fri 7AM-11PM, Weekends 9AM-8PM\n• **Features:** Digital resources, group study rooms, computer lab\n• **Special Collections:** African literature, Research archives"
    
    # Fees
    elif any(word in user_input for word in ["fee", "tuition", "cost", "payment", "financial", "scholarship"]):
        return "💰 **Financial Information:**\n• Tuition: Varies by program (Contact admissions)\n• **Scholarships Available:** Academic, Sports, Arts\n• **Payment Plans:** Installment options\n• **Financial Aid Office:** financialaid@aiu.edu\n• Work-study programs available"
    
    # Campus facilities
    elif any(word in user_input for word in ["campus", "facility", "building", "lab", "hostel", "dorm"]):
        return "🏛️ **AIU Campus Facilities:**\n• Modern lecture halls & smart classrooms\n• State-of-the-art science & computer labs\n• Sports complex\n• Student center with food court\n• Health & wellness center\n• On-campus housing & hostels"
    
    # Student services
    elif any(word in user_input for word in ["service", "support", "help", "counseling", "advising"]):
        return "👥 **Student Support Services:**\n• Academic advising & tutoring\n• Career counseling & placement\n• Health & psychological services\n• International student support\n• Disability resource center\n• Leadership development programs\n• 24/7 campus security"
    
    # Events
    elif any(word in user_input for word in ["event", "activity", "festival", "celebration", "cultural"]):
        return "🎉 **Campus Events & Traditions:**\n• **Annual Cultural Festival** - Food, music, dance\n• **Tech Innovation Fair** - Student projects showcase\n• **Sports Tournament Week** - Inter-department competitions\n• **Career Fair** - Top company recruiters\n• **Leadership Conferences** - Guest speakers\n• **Community Service Day** - Giving back together"
    
    # Contact information
    elif any(word in user_input for word in ["contact", "email", "phone", "number", "address", "location"]):
        return "📞 **Contact AIU:**\n• **Main Campus:** 123 Education City, AIU Main Campus\n• **Phone:** +254 796 352 397 / +254 748 759 496\n• **Admissions:** +254 725 841 885"
    
    # Internet search trigger
    elif any(word in user_input for word in ["search", "internet", "online", "web", "latest", "update", "current"]):
        return search_internet(user_input)
    
    # Thanks
    elif any(word in user_input for word in ["thank", "thanks", "appreciate"]):
        return "You're welcome! 😊 I'm happy to help you learn more about African International University!"
    
    # Goodbye
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! 👋 Best of luck with your journey at African International University!"
    
    # Default with internet search option
    else:
        return f"I'm not sure about '{user_input}'. Would you like me to search online for current AIU information about this? Or you can ask about:\n• Sports and athletics 🏀\n• Student clubs 🎭\n• Academic programs 📚\n• Campus facilities 🏛️\n• Admissions process 📝"

# Chat input
if prompt := st.chat_input("Ask about African International University..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get and display bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(0.5)
            response = get_school_response(prompt)
        st.write(response)
    
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})