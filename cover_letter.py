import google.generativeai as genai
import os
from dotenv import load_dotenv
import pathlib

load_dotenv()


def generate_cover_letter(internship):
	media = pathlib.Path(__file__).parents[0] / "assets"
	# print(media)

	genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
	model = genai.GenerativeModel("gemini-1.5-flash")
	pdf = genai.upload_file(media / "Resume.pdf")

	prompt = "Write a cover letter for the above internship opportunity. Use relevant parts of the attached resume. Keep it concise. Use at most 2035 characters. The cover letter should not contain places where the user/applicant needs to make modifications. It should be ready to submit in the application form"
	internship = internship + '\n\n' + prompt
	response = model.generate_content([internship, pdf])
	return response.text
