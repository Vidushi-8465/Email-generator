#Importing required modules 
#stremlit for building web app interface
#subprocess- lets python run system commands
import streamlit as st
import subprocess
import json

# Displays the title and short description on the front page 
st.title("📨 Email Generator (LLaMA 3 - Ollama)")
st.write("Generate emails locally using LLaMA 3 through Ollama.")

#inputs from User(Tone of email, Subj- on what topic the email is to be generated, Details of email i.e personalisation)
tone = st.selectbox("Select tone:", ["Formal", "Friendly", "Apologetic", "Persuasive"])
subject = st.text_input("Subject or topic:")
details = st.text_area("Extra details (optional):")

#Normal button for user 
if st.button("Generate Email"):
    # To validate a Input
    if not subject:
        st.warning("Please enter a subject.")
    else:
        # to create a prompt and build a natural language prompt for LLama
        prompt = f"Write a {tone.lower()} email about: {subject}. {details}"

        # running Ollama cmd i.e it runs the system cmd
        with st.spinner("Generating..."):
            process = subprocess.Popen(
                ["ollama", "run", "llama3", prompt],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            output, error = process.communicate()
        # To show if any error is generated or the generated email
        if error:
            st.error(error)
        else:
            st.subheader("✉️ Generated Email:")
            st.write(output)
