import streamlit as st

st.set_page_config(page_title="LowStim Games 🌿", page_icon="🌿", layout="centered")

st.markdown("<h1 style='text-align:center;'>🌿 LowStim Games</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>A pocket of calm for busy minds. Play slow, mindful mini-games made for adults.</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🪨 Rock Paper Scissors")
    st.write("A quiet classic. No rush — play when you feel like it.")
    st.page_link("pages/Rock Paper Scissors.py", label="Play")

with col2:
    st.markdown("### 🌊 Breathing Buddy")
    st.write("Breathe with the tide. A calming breathing exercise to slow down.")
    st.page_link("pages/Breathing Buddy.py", label="Play")

with col3:
    st.markdown("### ✏️ Number Guessing Game")
    st.write("Guess the number selected by the system.")
    st.page_link("pages/Number Guessing Game.py", label="Play")

st.markdown("---")
st.markdown("<p style='text-align:center; font-size:0.9rem;'>Built by <b>Sanya A</b> · A calm web experiment 🕯️</p>", unsafe_allow_html=True)
