import random
import streamlit as st

st.set_page_config(page_title="Number Guessing Game 🔢", page_icon="🔢", layout="centered")

st.title(f"Hello, welcome to the number guessing game.")
st.subheader(f"To begin, you need to enter a range of numbers.")
st.subheader(f"The game will then pick the winning number for you to guess.")

#User input for the number range
lower = st.number_input("Enter the Lower bound: ", value=None,format="%d",step=1)
upper = st.number_input("Enter the Upper bound: ", value=None,format="%d",step=1)


#Initializing session states
if "winning_number" not in st.session_state:
    st.session_state.winning_number = None
if "counter" not in st.session_state:
    st.session_state.counter = 0
if "chances" not in st.session_state:
    st.session_state.chances = 7
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "guesses" not in st.session_state:
    st.session_state.guesses = []  



#Start Game Button Logic
if st.button("Start Game"):
    if lower is not None and upper is not None and upper > lower:
        st.session_state.winning_number = random.randint(int(lower), int(upper)) #Selecting the winning number using random function
    st.session_state.game_started = True
    st.session_state.counter = 0
    st.session_state.guesses = []  
    st.text(f"\nThe number you need to guess has been selected by the game\nYou have 7 guesses before time runs out\nLet's begin guessing!")

#Guessing section

if st.session_state.game_started:
    guess = st.number_input("Guess your number: ", min_value=int(lower), max_value=int(upper), key="guess_input")
    if st.button("Submit Guess"):
            st.session_state.counter +=1
            if guess == st.session_state.winning_number:
                st.success(f"That's right! You guessed it in just {st.session_state.counter} attempt/s!")
                st.balloons()
                st.session_state.game_started = False
            elif st.session_state.counter >= st.session_state.chances and guess != st.session_state.winning_number:
                st.error(f"Oof, unfortunately, you're out of chances. The winning number was {st.session_state.winning_number}.")
                st.session_state.game_started = False
                st.session_state.guesses.append(guess)
            elif guess > st.session_state.winning_number:
                st.warning("Too high. Try a lower number.")
                st.session_state.guesses.append(guess)
            elif guess < st.session_state.winning_number:
                st.warning("Too low. Try a higher number.")
                st.session_state.guesses.append(guess)
            if st.session_state.guesses:
                st.info(f"Previous guesses: {st.session_state.guesses}")
    attempts_left = st.session_state.chances - st.session_state.counter
    st.text(f"Attempts left: {attempts_left}")


