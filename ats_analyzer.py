from sklearn.feature_extraction.text import CountVectorizer

def ats_keyword_analysis(cover_letter, job_description):
    cv = CountVectorizer()
    X = cv.fit_transform([cover_letter, job_description])
    features = cv.get_feature_names_out()
    
    # Count how many job keywords are present in the cover letter
    cover_letter_words = set(cover_letter.lower().split())
    job_keywords = set(job_description.lower().split())
    matched = cover_letter_words.intersection(job_keywords)
    
    score = len(matched) / len(job_keywords) * 100 if job_keywords else 0
    return score, list(matched)
