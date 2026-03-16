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

def extract_resume_text(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

    return text
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

resume_text = extract_resume_text("text_resume.pdf")

print("Resume Content:\n")
print(resume_text)

skills_found = detect_skills(resume_text)

print("\nDetected Skills:")
for skill in skills_found:
    print(skill)

job_skills = extract_job_skills(job_description)

score, matched, missing = calculate_ats_score(skills_found, job_skills)

print("\nJob Skills:", job_skills)

print("\nATS Score:", round(score,2), "%")

print("\nMatched Skills:")
for skill in matched:
    print(skill)

print("\nMissing Skills:")
for skill in missing:
    print(skill)