import streamlit as st
import random


st.set_page_config(page_title="Rock Paper Scissors 🪨", page_icon="🪨", layout="centered")


#st.title("Rock Paper Scissor!")

name = st.text_input("What is your name?", key="name")

if name:
    st.write(f"Hi {name}, pick one: ")

    user_choice = None
    if st.button("Rock", key='rock'):
        user_choice="rock"
    if st.button("Paper", key='paper'):
        user_choice="paper"
    if st.button("Scissor", key='scissor'):
        user_choice="scissor"

    if user_choice:
        elements = ["rock","paper","scissor"]
        game_choice = random.choice(elements)
        st.write(f"System picked: **{game_choice}**")\
    
        if user_choice == game_choice:
            st.warning(f"{name}, you tied with the game!")
        elif (user_choice == "rock" and game_choice == "scissor") or (user_choice == "scissor" and game_choice == "paper") or (user_choice == "paper" and game_choice == "rock"):
            st.success(f"You win, {name}! 🎉")
        else:
            st.error(f"You lose, {name}! 😢")

