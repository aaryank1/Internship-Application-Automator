# Internshala Job Application Automation

This repository contains a Python-based project that automates the process of applying for internships on Internshala. Using Selenium for browser automation and OpenAI's Generative AI for generating customized cover letters and answers to additional questions, this project simplifies the job application process.

---

## Features

- **Automated Login**: Logs into the Internshala platform using user-provided credentials.
- **Internship Discovery**: Filters and lists internships based on predefined preferences.
- **Custom Cover Letter Generation**: Generates personalized cover letters for each application using OpenAI's Gemini API.
- **Additional Questions Handling**: Automatically answers additional questions based on the internship description and resume content.
- **Resume Upload**: Automatically uploads the user's resume during the application process.
- **Human-like Interaction**: Includes randomized delays to mimic human behavior.

---

## Folder Structure

markdown
Copy code
# Internshala Job Application Automation

This repository contains a Python-based project that automates the process of applying for internships on Internshala. Using Selenium for browser automation and OpenAI's Generative AI for generating customized cover letters and answers to additional questions, this project simplifies the job application process.

---

## Features

- **Automated Login**: Logs into the Internshala platform using user-provided credentials.
- **Internship Discovery**: Filters and lists internships based on predefined preferences.
- **Custom Cover Letter Generation**: Generates personalized cover letters for each application using OpenAI's Gemini API.
- **Additional Questions Handling**: Automatically answers additional questions based on the internship description and resume content.
- **Resume Upload**: Automatically uploads the user's resume during the application process.
- **Human-like Interaction**: Includes randomized delays to mimic human behavior.

---

## Folder Structure
```
├── assets/
│   └── Resume.pdf            # Resume used for applications
├── main.py                   # Entry point of the project
├── jobautomate.py            # Base class for job automation
├── internshala.py            # Internshala-specific automation logic
├── additional_answer.py      # Generates answers to additional application questions
├── cover_letter.py           # Generates personalized cover letters
├── .env                      # Contains environment variables (credentials)
└── README.md                 # Project documentation
```
---

## Prerequisites

- Python 3.7+
- Google Chrome
- ChromeDriver (matching version)
- Selenium library
- OpenAI's Python SDK
- `dotenv` library for managing environment variables

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/internshala-automation.git
   cd internshala-automation

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

3. **Set up environment variables: Create a .env file in the root directory and add the following:**
    ```bash
    EMAIL=<your_internshala_email>
    PASSWORD=<your_internshala_password>
    INTERNSHALA_URL=https://internshala.com/internships
    GEMINI_API_KEY=<your_openai_api_key>

4. **Add your resume: Place your resume as a PDF file in the assets/ directory with the name Resume.pdf.**

## Usage
1. Run the script:
    ```bash
    python main.py

2. The script will log in to Internshala, find relevant internships, and apply to them by generating customized cover letters and answering any additional questions.

## Customization
- **Job Filters**: Modify the filtering logic in the find_jobs_and_apply method in internshala.py to include or exclude specific types of internships.
- **Resume and Cover Letter**: Update Resume.pdf and adapt the logic in generate_cover_letter to tailor applications further.

## Important Note

This script is compatible **only with Internshala accounts created using an email and password.** It does not support accounts that use "Sign in with Google" or other third-party authentication methods. Users must ensure they have registered on Internshala with an email and password to use this automation tool.



https://github.com/user-attachments/assets/a2e1503b-2327-4b83-84b1-469d63c8b0c3

