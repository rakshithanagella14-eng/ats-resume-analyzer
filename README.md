

# ATS Resume Analyzer using python

A web application that analyzes resumes and compares them with job descriptions to calculate an ATS (Applicant Tracking System) compatibility score.

Live Demo:
https://ats-resume-analyzer-gtnq.onrender.com

## Features

- Upload resume in PDF format
- Extract resume text automatically
- Detect technical skills from resume
- Compare resume skills with job description
- Calculate ATS compatibility score
- Display matched and missing skills
- Visualize results using charts

## Tech Stack

Backend:
Python
Flask

Libraries:
PyPDF2
Chart.js

Tools:
Git
GitHub
Render (for deployment)


## How It Works

1. User uploads a resume PDF.
2. User enters a job description.
3. The system extracts text from the resume.
4. Skills are detected from the resume.
5. Job description skills are identified.
6. ATS score is calculated based on skill matching.
7. Results are displayed with charts.


## Installation (Run Locally)

Clone the repository:

git clone https://github.com/rakshithanagella14-eng/ats-resume-analyzer.git

Go into the project folder:

cd ats-resume-analyzer

Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py

Open in browser:

http://127.0.0.1:5000


## Project Screenshots

### Home Page
![alt text](screenshots/homepage.png)

### Resume Upload
![alt text](screenshots/upload.png)

### ATS Analysis Result
![alt text](screenshots/results.png)
![alt text](<screenshots/ats score results.png>)

### ATS Analysis chart
![alt text](screenshots/chart.png)


## Future Improvements

- Support DOCX resume format
- Advanced NLP skill detection
- Resume suggestions for improvement
- Multiple job comparison


## Author

Nagella Rakshitha