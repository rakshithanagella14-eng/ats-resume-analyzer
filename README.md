
# 🚀 ATS Resume Intelligence System

A web-based application that analyzes resumes against job descriptions and calculates an **ATS compatibility score using a weighted skill-matching algorithm**.

🔗 **Live Demo:**  
👉 Try it here: https://ats-resume-analyzer-gtnq.onrender.com

---

# 🎯 Problem Statement

Most resumes are rejected by Applicant Tracking Systems (ATS) due to poor keyword alignment and missing critical skills.

This project simulates ATS behavior and helps users:
- Identify matching skills
- Detect missing critical skills
- Improve resume-job alignment

---

# ⚡ Key Features

- 📄 Upload and analyze PDF resumes  
- 🧠 Intelligent **skill detection system**  
- ⚖️ **Weighted ATS scoring algorithm** (prioritizes important skills)  
- 📊 Visual representation using charts  
- ❌ Missing skills identification  
- 💡 Automated **suggestion engine** for improvement  

---

# 🧠 Engineering Highlights

- Designed a **rule-based skill extraction engine**
- Implemented a **dynamic weighting system** for job-specific scoring
- Optimized performance using **set-based lookups**
- Built a **modular backend structure** for scalability
- Integrated frontend visualization using Chart.js

---

# 🛠 Tech Stack

| Layer       | Technology              |
|------------|------------------------|
| Backend     | Python, Flask          |
| Libraries   | PyPDF2                 |
| Frontend    | HTML, CSS, Chart.js    |
| Deployment  | Render                 |
| Tools       | Git, GitHub            |

---

# 🔄 System Workflow

1. User uploads resume (PDF)
2. Job description is provided
3. Resume text is extracted
4. Skills are detected from both inputs
5. Weighted scoring algorithm calculates ATS score
6. Missing skills + suggestions are generated
7. Results displayed with visualization

---

# 📸 Screenshots

### Home Page
![Home](screenshots/homepage.png)

### Upload Interface
![Upload](screenshots/upload.png)

### Results
![Results](screenshots/results.png)

### Chart Visualization
![Chart](screenshots/chart.png)

---

# ⚙️ Installation

```bash
git clone https://github.com/rakshithanagella14-eng/ats-resume-analyzer.git
cd ats-resume-analyzer
pip install -r requirements.txt
python main.py
```

---

# 📈 Future Improvements

- NLP-based skill extraction (instead of keyword matching)
- Support for DOCX resumes
- AI-based resume improvement suggestions
- Multi-job comparison feature

---

---

# 🧪 Development Note

This project was built in a short time frame to simulate rapid prototyping and iterative development.

The commit history reflects continuous improvements, debugging, and feature additions, similar to real-world development workflows.


# 👩‍💻 Author

**Nagella Rakshitha**