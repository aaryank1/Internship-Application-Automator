from internshala import InternshalaAutomation
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
internshala_url = os.getenv("INTERNSHALA_URL")


# Creating an internshala object and applying to relevant opportunities.
internshala_obj = InternshalaAutomation(username=username, password=password, url=internshala_url)
internshala_obj.login()
internshala_obj.find_jobs_and_apply()
