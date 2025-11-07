import streamlit as st
import time

# --- Page setup ---
st.set_page_config(page_title="Breathing Buddy 🌊", page_icon="🌊", layout="centered")

# --- Custom CSS for centering and animation ---
st.markdown(
    """
    <style>
    body {
        background-color: #e6f7ff;
        color: #00334d;
    }

    .centered {
        text-align: center;
    }

    .circle {
        margin: 30px auto;
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: linear-gradient(145deg, #a2d5f2, #7ec8e3);
        animation: pulse 4s ease-in-out infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.9; }
        50% { transform: scale(1.4); opacity: 1; }
        100% { transform: scale(1); opacity: 0.9; }
    }

    .instructions {
        font-size: 1.3rem;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown('<h1 class="centered">🌊 Breathing Buddy</h1>', unsafe_allow_html=True)
st.markdown('<p class="centered">Find your calm. Follow the circle’s rhythm and breathe with the tide.</p>', unsafe_allow_html=True)

# --- Start button ---
if st.button("Start Breathing 🌬️", use_container_width=True):
    st.session_state["started"] = True

# --- Breathing sequence ---
if "started" in st.session_state and st.session_state["started"]:
    st.markdown('<div class="circle"></div>', unsafe_allow_html=True)

    # Loop for 3 breathing cycles
    for _ in range(3):
        st.markdown('<p class="centered instructions">Inhale... 🌊</p>', unsafe_allow_html=True)
        time.sleep(4)

        st.markdown('<p class="centered instructions">Hold... 🤍</p>', unsafe_allow_html=True)
        time.sleep(4)

        st.markdown('<p class="centered instructions">Exhale... 🌬️</p>', unsafe_allow_html=True)
        time.sleep(4)
        st.empty()  # Clears previous instruction before next cycle

    st.markdown('<p class="centered instructions">Done. Breathe easy. 💙</p>', unsafe_allow_html=True)
    st.session_state["started"] = False

# --- Footer ---
st.markdown('<br><p class="centered" style="font-size:0.9rem;">A calm experiment by <b>LowStim Games</b> 🪶</p>', unsafe_allow_html=True)
