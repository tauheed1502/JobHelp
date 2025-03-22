import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

def parse_cv(cv_text):
    """
    Parse a CV and extract key information such as skills, education, and experience.
    """
    doc = nlp(cv_text)
    
    # Extract skills, education, and experience using spaCy's named entity recognition (NER)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    education = [ent.text for ent in doc.ents if ent.label_ == "EDU"]
    experience = [ent.text for ent in doc.ents if ent.label_ == "EXPERIENCE"]
    
    return {
        "skills": skills,
        "education": education,
        "experience": experience
    }

def optimize_cv(cv_text, job_description):
    """
    Optimize a CV by aligning it with a job description using TF-IDF and cosine similarity.
    """
    # Vectorize the CV and job description
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([cv_text, job_description])
    
    # Calculate cosine similarity between the CV and job description
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    # Provide feedback on how to optimize the CV
    if similarity_score < 0.5:
        return "Your CV needs significant optimization to match the job description. Focus on adding relevant skills and experience."
    elif similarity_score < 0.8:
        return "Your CV is somewhat aligned with the job description. Consider adding more keywords and tailoring your experience."
    else:
        return "Your CV is well-optimized for this job description. Good job!"

def score_cv(cv_text, job_description):
    """
    Score a CV based on its alignment with a job description.
    """
    # Vectorize the CV and job description
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([cv_text, job_description])
    
    # Calculate cosine similarity between the CV and job description
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    # Convert similarity score to a percentage
    return int(similarity_score * 100)

# Example usage
cv_text = "Experienced software engineer with 5 years of experience in Python, Java, and machine learning. Master's degree in Computer Science."
job_description = "We are looking for a software engineer with expertise in Python, machine learning, and data analysis. A Master's degree in Computer Science is preferred."

parsed_cv = parse_cv(cv_text)
print("Parsed CV:", parsed_cv)

optimization_feedback = optimize_cv(cv_text, job_description)
print("Optimization Feedback:", optimization_feedback)

cv_score = score_cv(cv_text, job_description)
print("CV Score:", cv_score)