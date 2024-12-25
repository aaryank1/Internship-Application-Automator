from internshala import InternshalaAutomation
from naukri import Naukri
import os
from dotenv import load_dotenv

load_dotenv()

# Internshala
username = os.getenv("EMAIL")
internshala_password = os.getenv("INTERNSHALA_PASSWORD")
internshala_url = os.getenv("INTERNSHALA_URL")

internshala_obj = InternshalaAutomation(username=username, password=internshala_password, url=internshala_url)
internshala_obj.login()
internshala_obj.apply()


# Naukri.com
naukri_url = os.getenv("NAUKRI_URL")
naukri_password = os.getenv("NAUKRI_PASSWORD")

job = Naukri(username=username, password=naukri_password, url=naukri_url)
job.login()
job.apply()
