from flask import Flask, render_template, request
import os

if not os.path.exists("uploads"):
    os.makedirs("uploads")
from sample import extract_resume_text, detect_skills, extract_job_skills, calculate_ats_score

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    matched = []
    missing = []

    if request.method == "POST":
        file = request.files["resume"]
        job_description = request.form["job_description"]

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        resume_text = extract_resume_text(filepath)
        resume_skills = detect_skills(resume_text)
        job_skills = extract_job_skills(job_description)

        score, matched, missing = calculate_ats_score(resume_skills, job_skills)

    return render_template(
        "index.html",
        score=score,
        matched=matched,
        missing=missing
    )

if __name__ == "__main__":
    app.run(debug=True)