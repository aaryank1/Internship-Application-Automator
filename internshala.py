from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from jobautomate import JobAutomation
from dotenv import load_dotenv
import os
import time
from cover_letter import generate_cover_letter

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
internshala_url = os.getenv("INTERNSHALA_URL")

class InternshalaAutomation(JobAutomation):
	def login(self):
		self.driver.get("https://internshala.com/")

		login = self.driver.find_element(By.XPATH, value='//*[@id="header"]/div/nav/div[3]/button[2]')
		login.click()

		email_input = self.driver.find_element(By.NAME, value='email')
		pwd_input = self.driver.find_element(By.NAME, value='password')
		email_input.send_keys(self.username)
		pwd_input.send_keys(self.password)

		login_btn = self.driver.find_element(by=By.ID, value='modal_login_submit')
		login_btn.click()
		time.sleep(3)

	def fill_form(self, internship):
		try:
			time.sleep(1)
			cover_letter_container = self.driver.find_element(by=By.CSS_SELECTOR, value="#cover_letter_holder .ql-editor")
			cover_letter_text = generate_cover_letter(internship)
			cover_letter_container.send_keys(cover_letter_text)
			# time.sleep(10)
		except:
			print("No cover letter input box found")
			pass

	def find_jobs_and_apply(self):
		self.driver.get(internshala_url)
		list_of_jobs = self.driver.find_elements(by=By.CSS_SELECTOR, value='#internship_list_container_1 .visibilityTrackerItem')

		job_links = []
		for job in list_of_jobs:
			try:
				# print(job.find_element(by=By.CSS_SELECTOR, value="div div div h3").text)
				job_links.append(job.get_attribute("id"))
			except:
				continue

		# print(job_links)
		original_window = self.driver.current_window_handle
		for link in job_links:
			job = self.driver.find_element(by=By.ID, value=link)
			job.click()
			self.driver.switch_to.window(self.driver.window_handles[2])
			self.driver.close()
			self.driver.switch_to.window(self.driver.window_handles[1])

			internship = self.driver.find_element(by=By.CLASS_NAME, value="detail_view").text
			try:
				exclude_text = self.driver.find_element(by=By.CLASS_NAME, value="training_skills_container").text
				internship = internship.replace(exclude_text, "")
			except:
				pass

			time.sleep(2)

			apply_btn = self.driver.find_element(by=By.ID, value="apply_now_button")
			apply_btn.click()

			proceed_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="layout_table"]/div[5]/button')
			proceed_btn.click()

			self.fill_form(internship)
			self.driver.close()

			self.driver.switch_to.window(original_window)
			time.sleep(2)


internshala = InternshalaAutomation(email, password, url=internshala_url)
internshala.login()
internshala.find_jobs_and_apply()
