from typing import List, Dict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ResumeRanker:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        
    async def rank_resumes(self, job_description: str, resumes: List[str]) -> List[Dict[str, float]]:
        documents = [job_description] + resumes
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        
        job_description_vector = tfidf_matrix[0:1]
        resume_vectors = tfidf_matrix[1:]
        
        similarities = cosine_similarity(job_description_vector, resume_vectors)[0]
        
        ranked_results = [
            {"resume_index": idx, "score": float(score)}
            for idx, score in enumerate(similarities)
        ]
        
        return sorted(ranked_results, key=lambda x: x["score"], reverse=True) 