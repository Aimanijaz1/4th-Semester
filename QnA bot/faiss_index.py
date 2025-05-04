import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from medical_data import medical_qa_data

model = SentenceTransformer('all-MiniLM-L6-v2')

questions = [item["question"] for item in medical_qa_data]
answers = [item["answer"] for item in medical_qa_data]

# Encode questions
embeddings = model.encode(questions, convert_to_numpy=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def get_answer(user_query):
    query_embedding = model.encode([user_query])
    D, I = index.search(query_embedding, k=1)
    if D[0][0] < 1.0:  # Threshold
        return answers[I[0][0]]
    else:
        return "I'm sorry, I couldn't understand. Can you rephrase your question?"
