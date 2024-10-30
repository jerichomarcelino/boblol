import streamlit as st
from openai import OpenAI
from App_Pic import get_image, filename_from_input
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are Bob. Show a report of your teen driving performance"}, 
            {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content

# Create Streamlit UI
st.title("Bob - Teen Driving Report")

# Get user input through Streamlit
prompt = st.text_input("Enter your prompt:")

if st.button("Generate Report and Images"):
    if prompt:
        # Get text response
        response = get_completion(prompt)
        st.write("Bob's Report:")
        st.write(response)
        
        # Generate and display images
        image_response = get_image(prompt)
        st.write("Generated Images:")
        
        # Get the base filename without extension
        base_filename = filename_from_input(prompt)
        
        # Display the images directly using their filenames
        for i in range(2):  # Since we're generating 2 images
            image_path = f"{base_filename}_{i+1}.png"
            if os.path.exists(image_path):
                st.image(image_path, caption=f"Generated Image {i+1}")
