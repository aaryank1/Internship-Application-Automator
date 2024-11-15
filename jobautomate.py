from selenium import webdriver

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
chrome_opts.add_argument("start-maximized")


class JobAutomation:
	def __init__(self, username, password, url):
		self.username = username
		self.password = password
		self.url = url
		self.driver = webdriver.Chrome(options=chrome_opts)

	def login(self):
		pass

	def apply(self):
		pass

	def quit(self):
		self.driver.quit()
