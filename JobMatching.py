from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_jobs(cv_text, job_postings):
    """
    Match a CV with a list of job postings using TF-IDF and cosine similarity.
    """
    # Extract job descriptions from job postings
    job_descriptions = [job["description"] for job in job_postings]
    
    # Vectorize the CV and job descriptions
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([cv_text] + job_descriptions)
    
    # Calculate cosine similarity between the CV and each job description
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    
    # Rank job postings based on similarity scores
    ranked_jobs = []
    for i, job in enumerate(job_postings):
        job["similarity_score"] = similarity_scores[0][i]
        ranked_jobs.append(job)
    
    # Sort jobs by similarity score (descending order)
    ranked_jobs = sorted(ranked_jobs, key=lambda x: x["similarity_score"], reverse=True)
    
    return ranked_jobs

# Example usage
cv_text = "Experienced software engineer with 5 years of experience in Python, Java, and machine learning. Master's degree in Computer Science."

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

ranked_jobs = match_jobs(cv_text, job_postings)
print("Ranked Job Matches:")
for job in ranked_jobs:
    print(f"Title: {job['title']}\nDescription: {job['description']}\nLocation: {job['location']}\nSalary: {job['salary']}\nSimilarity Score: {job['similarity_score']:.2f}\n")