import PyPDF2 #resume reader
#skill database
skill_weights = {
    "python": 3,
    "flask": 3,
    "django": 2,
    "sql": 2,
    "html": 1,
    "css": 1,
    "javascript": 2,
    "api": 3,
    "backend": 3
}
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
    "embedded systems",
    "api", "backend"
]

#extract resume
def extract_resume_text(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text

#required skills
job_description = """
Looking for a Python developer and java developer with knowledge of SQL, Git,
Machine Learning, and Data Analysis.
"""
#skill detection for resume
def detect_skills(resume_text):
    resume_text = resume_text.lower()
    detected = set()

    for skill in skills_db:
        if skill in resume_text:
            detected.add(skill)

    return list(detected)

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
    score = 0
    total = 0
    matched_skills = []
    missing_skills = []
    job_skills = set(job_skills)
    # copy weights
    local_weights = skill_weights.copy()

    # add dynamic weights BEFORE scoring
    for skill in job_skills:
        if skill not in local_weights:
            local_weights[skill] = 2

    # suggestion mapping
    suggestions_map = {
        "python": "Add Python projects or mention Python experience",
        "flask": "Include backend API development using Flask",
        "sql": "Add database handling experience",
        "api": "Mention REST API development",
        "backend": "Add backend-related projects"
    }

    suggestions = set()
    resume_skills = set(resume_skills)
    for skill, weight in local_weights.items():

        if skill in job_skills:
            total += weight

            if skill in resume_skills:
                score += weight
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

                if skill in suggestions_map:
                    suggestions.add(suggestions_map[skill])

    if total == 0:
        ats_score = 0
    else:
        ats_score = int((score / total) * 100)
    matched_skills.sort()
    missing_skills.sort()
    
    return ats_score, matched_skills, missing_skills, sorted(list(suggestions))