#streamlit
import streamlit as st # type: ignore

st.set_page_config(page_title="growth mindset project",project_icon="✹")

st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to your Growth Journey")
st.write("This is the beginning of an exciting path where every step you take brings new opportunities to learn, improve, and achieve your goals. Growth is not just about reaching a destination; it's about embracing challenges, gaining knowledge, and evolving into the best version of yourself. Stay consistent, stay curious, and remember—every small effort counts. Keep pushing forward, and success will follow! 🌟")

#quote section
st.header("Daily Quote to Inspire Your Growth Mindset ✨")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.– Winston ChurchillEvery day is a new opportunity to grow, learn, and improve. Embrace challenges with a positive mindset, believe in your potential, and keep moving forward. Your journey to success is built on persistence and resilience. Stay inspired, stay motivated! 🚀")

st.header("What's Your Challenge Today? 💪")
user_input = st.text_input("Discribe a challenge you're facing today: ")

#condition
if user_input:
    st.success(f"You're facing: {user_input}. keep pushing forward! 🚀 ")
else:
    st.warning("💬 Tell Us About Your Challenge to Get Started! 💬")

#reflexing
st.header("🌱 Reflect on Your Growth and Progress 🌱")
reflection = st.text_area("Write down your thoughts and feelings about your progress:")

if reflection:
    st.success(f"Great Insight! {reflection} Keep reflecting and growing!")
else:
    st.info("🔍 Reflecting on Past Experiences Helps You Grow! 🔍")

#achievements
st.header("🎉 Celebrate Your Wins! 🎉")
achievment = st.text_input(":🏆 Share Something You’ve Recently Accomplished! 🏆")

if achievment:
    st.success(f"🌟 Amazing! You Achieved It!:{achievment} 🌟")
else:
    st.info("🎉 Big or Small, Every Achievement Counts! 🎉")

#footer
st.write("- - -")
st.write("🌟 Keep Believing in Yourself – Growth is a Journey! 🌟")

st.write("✨ Created by Muhammad Tahir Hasni ✨")