import streamlit as st
import random
from pathlib import Path

# File path
path = Path.cwd()
p = path / "Fake_News_Paper.txt"

st.title("📰 Fake News Generator")

# Category selection
category = st.selectbox(
    "Choose Category",
    ["Politics", "Sports", "Entertainment", "Science"]
)

# User custom input option
custom = st.checkbox("Use Custom Input")

# ---------------- CUSTOM INPUT ---------------- #

if custom:

    own_name = st.text_input("Enter Name")
    own_action = st.text_input("Enter Action")
    own_place = st.text_input("Enter Place")

    if st.button("Generate Custom Fake News"):

        sentence = f"{own_name} {own_action} {own_place}"

        st.success(sentence)

        with open(p, "a", encoding="utf-8") as fs:
            fs.write(sentence + "\n")

        st.success("Saved to file successfully!")

# ---------------- RANDOM GENERATION ---------------- #

else:

    if st.button("Generate Random Fake News"):

        if category == "Politics":
            names = ['Rahul Gandhi', 'Narendra Modi', 'Mamta Banerjee']
            actions = ['became PM of', 'won election in', 'visited']
            places = ['USA', 'UK', 'China']

        elif category == "Sports":
            names = ['Sachin Tendulkar', 'Virat Kohli', 'Neeraj Chopra']
            actions = ['played cricket in', 'won gold medal in', 'became coach of']
            places = ['Australia', 'Japan', 'Dubai']

        elif category == "Entertainment":
            names = ['Shahrukh Khan', 'Brad Pitt', 'Jackie Chan']
            actions = ['acted in movie at', 'performed dance in', 'opened studio in']
            places = ['Hollywood', 'Bollywood', 'Korea']

        elif category == "Science":
            names = ['Albert Einstein', 'Isaac Newton', 'Nikola Tesla']
            actions = ['invented AI in', 'discovered theory in', 'created robot in']
            places = ['Switzerland', 'NASA', 'Germany']

        sentence = f"{random.choice(names)} {random.choice(actions)} {random.choice(places)}"

        st.success(sentence)

        # Save to file
        with open(p, "a", encoding="utf-8") as fs:
            fs.write(sentence + "\n")

        st.success("Saved to file successfully!")

# ---------------- SHOW SAVED NEWS ---------------- #

if st.button("Show Saved Fake News"):

    if p.exists():

        with open(p, "r", encoding="utf-8") as fs:
            content = fs.read()

        st.text_area("Saved News", content, height=300)

    else:
        st.warning("No file found!")