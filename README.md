🧾 Resume/CV Ranker

A FastAPI-based application that ranks resumes/CVs against job descriptions using NLP and cosine similarity.

Features:
- Async FastAPI implementation
- TF-IDF and cosine similarity for ranking
- Modular project structure
- RESTful API endpoint

Setup:
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python run.py
```

API Usage:
POST /api/rank
```json
{
    "job_description": "Your job description here",
    "resumes": ["Resume 1 text", "Resume 2 text", ...]
}
```

The API will return ranked results with similarity scores.