import PyPDF2 #resume reader
#skill database
skills_db = [
    "python",
    "java",
    "c++",
    "machine learning",
    "data analysis",
    "sql",
    "git",
    "flask",
    "django",
    "matlab",
    "iot",
    "embedded systems"
]

#extract resume
def extract_resume_text(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

    return text

#required skills
job_description = """
Looking for a Python developer and java developer with knowledge of SQL, Git,
Machine Learning, and Data Analysis.
"""
#skill detection for resume
def detect_skills(resume_text):
    resume_text = resume_text.lower()
    detected = []

    for skill in skills_db:
        if skill in resume_text:
            detected.append(skill)

    return detected

#resume skill match
def extract_job_skills(job_text):
    job_text = job_text.lower()
    job_skills = []

    for skill in skills_db:
        if skill in job_text:
            job_skills.append(skill)

    return job_skills

#ats sccore
def calculate_ats_score(resume_skills, job_skills):
    matched = []
    missing = []

    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(job_skills)) * 100

    return score, matched, missing

