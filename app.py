import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="LowStim Games 🌿", page_icon="🌿", layout="centered")

# --- Custom style ---
st.markdown("""
<style>
body {
    background-color: #f5f9fc;
    color: #1f2937;
    font-family: 'Inter', sans-serif;
}
h1, h2, h3, p {
    text-align: center;
}
.card {
    background-color: #ffffff;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transition: all 0.2s ease-in-out;
}
.card:hover {
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# --- Main Title ---
st.markdown("<h1>🌿 LowStim Games</h1>", unsafe_allow_html=True)
st.markdown("<p>A pocket of calm for busy minds. Play slow, mindful mini-games made for adults.</p>", unsafe_allow_html=True)

st.markdown("---")

# --- Game cards ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🪨 Rock Paper Scissors")
    st.write("A quiet classic. No rush — play when you feel like it.")
    st.link_button("Play", "https://share.streamlit.io/sanyaambegaokar/lowstim-games/games/rps_streamlit.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🌊 Breathing Buddy")
    st.write("Breathe with the tide. A calming breathing exercise to slow down.")
    st.link_button("Play", "https://share.streamlit.io/sanyaambegaokar/lowstim-games/games/breathing-buddy.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("<p style='text-align:center; font-size:0.9rem;'>Built by <b>Sanya A</b> · A calm web experiment 🕯️</p>", unsafe_allow_html=True)
