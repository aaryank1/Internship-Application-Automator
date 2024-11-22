from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from jobautomate import JobAutomation
import os
import time
from cover_letter import generate_cover_letter
from additional_answer import generate_ans


class InternshalaAutomation(JobAutomation):
	def login(self):
		self.driver.get("https://internshala.com/")

		login = self.driver.find_element(By.XPATH, value='//*[@id="header"]/div/nav/div[3]/button[2]')
		login.click()

		email_input = self.driver.find_element(By.NAME, value='email')
		pwd_input = self.driver.find_element(By.NAME, value='password')

		# The random sleep() and clicks are used as an attempt to mimic human behaviour to bypass captcha
		time.sleep(2)
		pwd_input.click()
		time.sleep(1)
		email_input.click()
		email_input.send_keys(self.username)
		time.sleep(3)
		pwd_input.click()
		pwd_input.send_keys(self.password)

		login_btn = self.driver.find_element(by=By.ID, value='modal_login_submit')
		login_btn.click()
		time.sleep(3)

	def fill_form(self, internship):
		# Check and fill Cover letter
		try:
			time.sleep(1)
			cover_letter_container = self.driver.find_element(by=By.CSS_SELECTOR, value="#cover_letter_holder .ql-editor")
			cover_letter_text = generate_cover_letter(internship)
			cover_letter_container.send_keys(cover_letter_text)
		except:
			pass

		# Availability
		try:
			availability = self.driver.find_elements(by=By.CSS_SELECTOR,value="#confirm_availability_container #options .radio")
			no_btn = availability[1].find_element(by=By.TAG_NAME, value="label").click()

			reason = self.driver.find_element(by=By.ID, value="confirm_availability_textarea")
			reason.send_keys("No, Dear Hiring Team,\nI wanted to inform you about my availability for the internship. I have college exams until 9th December, so I would be able to join from 10th December. However, I will be unavailable from 29th December to 2nd January due to prior commitments.\nI would greatly appreciate your understanding and request either a brief leave during that period or the possibility to start the internship from 3rd January onwards.\nPlease let me know if this can be accommodated. I am eager to contribute and am flexible to discuss arrangements that work best for your team.\nThank you for your time and consideration.\nBest regards,\nAaryan Kakade.")
		except:
			print("No option detected")
			pass

		# Resume Upload
		resume = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets", "Resume.pdf"))
		rem_prefilled_resume = self.driver.find_element(by=By.CSS_SELECTOR, value=".custom-resume-container .file-frame-container .frame-close i")
		rem_prefilled_resume.click()
		file_input = self.driver.find_element(by=By.CSS_SELECTOR, value="input[type='file']")
		file_input.send_keys(resume)

		# Laptop and Internet availability
		try:
			laptop_internet_question = self.driver.find_elements(by=By.CLASS_NAME, value="additional_question")
			for q in laptop_internet_question:
				try:
					label = q.find_element(by=By.CSS_SELECTOR, value=".custom_question_boolean_container .radio label")
					label.click()
				except:
					continue
		except:
			# print("No laptop question or other error")
			pass

		# Custom Additional Questions
		additional_questions = self.driver.find_elements(by=By.CLASS_NAME, value="additional_question")
		for question in additional_questions:
			try:
				que = question.find_element(by=By.CLASS_NAME, value="assessment_question").text
				textarea = question.find_element(by=By.CLASS_NAME, value="custom-question-answer")
				answer = generate_ans(que, internship)
				textarea.send_keys(answer)
			# print(answer)

			except:
				print("No additional questions")
				continue

		submit_btn = self.driver.find_element(by=By.ID, value="submit")
		submit_btn.click()
		time.sleep(4)


	def find_jobs_and_apply(self):
		self.driver.get(self.url)
		list_of_jobs = self.driver.find_elements(by=By.CSS_SELECTOR, value='#internship_list_container_1 .visibilityTrackerItem')

		job_links = []
		for job in list_of_jobs:
			try:
				job_title = job.find_element(by=By.CSS_SELECTOR, value="div div div h3").text
				job_title = job_title.lower()

				# Here I have manually filtered out jobs that I do not want to apply to. If you want to apply to these as well, remove this line.
				if "wordpress" not in job_title and "nextjs" not in job_title and "php" not in job_title:
					# print(job_title)
					job_links.append(job.get_attribute("id"))
			except:
				continue

		original_window = self.driver.current_window_handle
		for link in job_links:
			job = self.driver.find_element(by=By.CSS_SELECTOR, value=f"#{link} h3 a")
			job.click()
			self.driver.switch_to.window(self.driver.window_handles[1])

			# Extract the details of the internship. We need this for gemini to fill the internship application form.
			internship = self.driver.find_element(by=By.CLASS_NAME, value="detail_view").text
			try:
				# These are advertisements for courses that need to be removed from the internship details.
				exclude_text = self.driver.find_element(by=By.CLASS_NAME, value="training_skills_container").text
				internship = internship.replace(exclude_text, "")
			except:
				pass

			try:
				apply_btn = self.driver.find_element(by=By.ID, value="apply_now_button")
				apply_btn.click()

				proceed_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="layout_table"]/div[5]/button')
				proceed_btn.click()

				self.fill_form(internship)
				self.driver.close()

				self.driver.switch_to.window(original_window)
				time.sleep(2)
			except:
				apply_btn = self.driver.find_element(by=By.ID, value="easy_apply_button")
				apply_btn.click()

				self.fill_form(internship)
				self.driver.close()

				self.driver.switch_to.window(original_window)
				time.sleep(2)

