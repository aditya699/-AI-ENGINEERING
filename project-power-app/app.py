import os
from dotenv import load_dotenv
import pandas as pd
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini API
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

def classify_email(row):
    prompt = f"""
    Classify the following email into one of these categories: Marketing Team, Quality Team, or Finance Team.
    Only respond with the team name.
    
    Subject: {row['Subject']}
    Email Content: {row['Email']}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# Read the Excel file
df = pd.read_excel('data.xlsx')

# Apply the classification function to each row
df['Team'] = df.apply(classify_email, axis=1)

# Save the results to a new Excel file
df.to_excel('Classified_Emails_Gemini.xlsx', index=False)

print("Classification complete. Results saved to 'Classified_Emails_Gemini.xlsx'.")