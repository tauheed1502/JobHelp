from flask import Flask, request, render_template_string
from cv_processing import parse_cv, optimize_cv, score_cv
from job_matching import match_jobs

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CV Optimization and Job Matching</title>
</head>
<body>
    <h1>AI-Driven CV Optimization and Job Matching</h1>
    <form method="POST">
        <textarea name="cv_text" rows="10" cols="50" placeholder="Paste your CV here..."></textarea><br><br>
        <input type="submit" value="Optimize and Match Jobs">
    </form>
    {% if feedback %}
    <h2>Optimization Feedback:</h2>
    <p>{{ feedback }}</p>
    <h2>CV Score:</h2>
    <p>{{ cv_score }}%</p>
    <h2>Job Matches:</h2>
    <ul>
        {% for job in ranked_jobs %}
        <li>
            <strong>Title:</strong> {{ job['title'] }}<br>
            <strong>Description:</strong> {{ job['description'] }}<br>
            <strong>Location:</strong> {{ job['location'] }}<br>
            <strong>Salary:</strong> {{ job['salary'] }}<br>
            <strong>Similarity Score:</strong> {{ job['similarity_score'] | round(2) }}
        </li>
        {% endfor %}
    </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    cv_score = None
    ranked_jobs = None
    
    if request.method == "POST":
        cv_text = request.form["cv_text"]
        
        # Example job postings
        job_postings = [
            {
                "title": "Software Engineer",
                "description": "We are looking for a software engineer with expertise in Python, machine learning, and data analysis.",
                "location": "New York",
                "salary": "$100,000 - $120,000"
            },
            {
                "title": "Senior Data Scientist",
                "description": "Senior data scientist role requiring experience in machine learning, Python, and big data.",
                "location": "San Francisco",
                "salary": "$130,000 - $150,000"
            },
            {
                "title": "Front-End Developer",
                "description": "Front-end developer with expertise in JavaScript, React, and UI/UX design.",
                "location": "Chicago",
                "salary": "$90,000 - $110,000"
            }
        ]
        
        # Get optimization feedback
        feedback = optimize_cv(cv_text, job_postings[0]["description"])
        
        # Get CV score
        cv_score = score_cv(cv_text, job_postings[0]["description"])
        
        # Get ranked job matches
        ranked_jobs = match_jobs(cv_text, job_postings)
    
    return render_template_string(HTML_TEMPLATE, feedback=feedback, cv_score=cv_score, ranked_jobs=ranked_jobs)

if __name__ == "__main__":
    app.run(debug=True)