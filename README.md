BOB - Your Teen Driving Report Generator

What is this?
This is an AI-powered application that creates detailed teen driving reports and generates related images. It uses OpenAI's GPT for writing reports and DALL-E for creating images.

Features:
- Generates detailed driving performance reports
- Creates AI images related to the driving scenario
- Easy-to-use web interface
- Secure API key handling

How to Set Up:
1. Clone this repository to your computer:
   git clone https://github.com/Reenamjot/boblol.git
   cd boblol

2. Install required packages:
   pip install streamlit openai python-dotenv requests pillow

3. Set up your API key:
   - Copy .env.example to a new file named .env
   - Add your OpenAI API key to the .env file
   - Never share your .env file!

4. Run the app:
   streamlit run App_UI.py

How to Use:
1. Open the app in your web browser
2. Type your driving scenario or question in the text box
3. Click "Generate Report and Images"
4. View your personalized driving report and AI-generated images

Files in this Project:
- App_UI.py: Main application interface
- App_Pic.py: Handles image generation
- .env: Stores your API key (you need to create this)
- .env.example: Shows what should go in your .env file
- README.md: This file

Requirements:
- Python 3.8 or higher
- OpenAI API key
- Internet connection
- Required Python packages (listed in setup instructions)

Created by: [Your Name]
Last Updated: [Current Date]
