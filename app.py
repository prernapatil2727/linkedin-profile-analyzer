from google import genai
from fpdf import FPDF
import os

client = genai.Client(api_key="Gemini_API_KEY")

headline = input("Enter LinkedIn Headline: ")
about = input("Enter About Section: ")
skills = input("Enter Skills: ")
experience = input("Enter Experience: ")

prompt = f"""
Analyze this LinkedIn profile:

Headline: {headline}
About: {about}
Skills: {skills}
Experience: {experience}

Give:
- Score (0-100)
- Strengths
- Weaknesses
- Improvements
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

report = response.text

os.makedirs("output", exist_ok=True)

def clean_text(text):
    return text.encode("latin-1", "ignore").decode("latin-1")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.multi_cell(0, 10, "LINKEDIN PROFILE REPORT\n\n")
pdf.multi_cell(0, 10, clean_text(report))

pdf.output("output/report.pdf")
print("Report generated successfully!")
