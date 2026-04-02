from flask import Flask, render_template, request
import os
import uuid

from sample import extract_resume_text, detect_skills, extract_job_skills, calculate_ats_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    matched = []
    missing = []
    suggestions = []

    if request.method == "POST":

        if "resume" not in request.files:
            return "No file uploaded"

        file = request.files["resume"]

        if file.filename == "":
            return "No file selected"

        if not file.filename.endswith(".pdf"):
            return "Only PDF files allowed"

        job_description = request.form["job_description"]

        # unique filename (prevents overwrite)
        filename = str(uuid.uuid4()) + ".pdf"
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # processing
        resume_text = extract_resume_text(filepath)
        resume_skills = detect_skills(resume_text)
        job_skills = extract_job_skills(job_description)

        score, matched, missing, suggestions = calculate_ats_score(
            resume_skills, job_skills
        )

    return render_template(
        "index.html",
        score=score,
        matched=matched,
        missing=missing,
        suggestions=suggestions
    )


if __name__ == "__main__":
    app.run(debug=True)