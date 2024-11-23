from jobautomate import JobAutomation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time


load_dotenv()

username = os.getenv("EMAIL")
password = os.getenv("NAUKRI_PASSWORD")


class Naukri(JobAutomation):
	def login(self):
		self.driver.get("https://www.naukri.com/")
		login_section = self.driver.find_element(by=By.ID, value="login_Layer")
		login_section.click()

		wait = WebDriverWait(self.driver, 10)
		login_form = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-layer form")))
		credentials = login_form.find_elements(by=By.CLASS_NAME, value='form-row')
		email = credentials[0].find_element(by=By.TAG_NAME, value="input")
		email.send_keys(username)
		pwd = credentials[1].find_element(by=By.TAG_NAME, value="input")
		pwd.send_keys(password)

		submit_btn = login_form.find_element(by=By.TAG_NAME, value="button")
		submit_btn.click()
		time.sleep(2)

	def apply(self):
		self.driver.get(self.url)
		wait = WebDriverWait(self.driver, 5)
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#listContainer .srp-jobtuple-wrapper")))
		opportunities_list = self.driver.find_elements(by=By.CSS_SELECTOR, value="#listContainer div div .srp-jobtuple-wrapper")

		opp_list = []
		for opp in opportunities_list:
			try:
				opp_link = opp.find_element(by=By.CSS_SELECTOR, value=".cust-job-tuple [class=' row1'] a")
				opp_list.append(opp_link)
			except Exception as e:
				print(f"Error Finding Error {e}")

		original_window = self.driver.current_window_handle
		for opp in opp_list:
			opp.click()
			self.driver.switch_to.window(self.driver.window_handles[1])
			try:
				self.driver.find_element(By.ID, "apply-button")
				wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#job_header #apply-button")))
				apply_btn = self.driver.find_element(by=By.XPATH, value="//button[text()='Apply']")
				apply_btn.click()
			except:
				print("Application at Company")
				pass
			self.driver.close()
			self.driver.switch_to.window(original_window)
