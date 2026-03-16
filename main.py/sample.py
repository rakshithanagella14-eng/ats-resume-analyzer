import PyPDF2
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
def detect_skills(resume_text):
    resume_text = resume_text.lower()
    detected = []

    for skill in skills_db:
        if skill in resume_text:
            detected.append(skill)

    return detected

def extract_resume_text(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

    return text


resume_text = extract_resume_text("text_resume.pdf")

print("Resume Content:\n")
print(resume_text)
skills_found = detect_skills(resume_text)

print("\nDetected Skills:")
for skill in skills_found:
    print(skill)
