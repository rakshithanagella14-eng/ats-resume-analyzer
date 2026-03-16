import PyPDF2

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