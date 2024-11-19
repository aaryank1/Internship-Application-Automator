import google.generativeai as genai
from dotenv import load_dotenv
import os
import pathlib


def generate_ans(question, opportunity):
	media = pathlib.Path(__file__).parents[0] / "assets"

	genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
	model = genai.GenerativeModel("gemini-1.5-flash")
	pdf = genai.upload_file(media / "Resume.pdf")

	prompt = """
	Answer the above question on the applicants behalf, based on the attached resume and job/internship opportunity post.
	Follow these rules while generating a response:
	1) Use relevant parts of the attached resume.
	2) Keep it concise.
	3)The answer should not contain places where the user/applicant needs to make modifications. It should be ready to submit in the application form.
	4)Do not use markdown syntax.
	5)If the question asks for adding project links or attachments, extract and return only the GitHub link from the attached resume. Provide no additional text or explanation for these questions. For all other questions, answer the question properly with descriptive and relevant responses, ensuring there are no blank parts requiring user modifications. Do not include the question in your response."""
	question = f'internship opportunity post: "{opportunity}"\nQuestion asked in application form: \n"{question}"\n\n+ {prompt}'
	response = model.generate_content([question, pdf])
	# print(response.text)
	return response.text
