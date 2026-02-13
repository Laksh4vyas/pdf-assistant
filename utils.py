import os
import numpy as np
import faiss
import PyPDF2
import google.generativeai as genai
from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            t = page.extract_text()
            if t: text += t
    return text

def split_text(text, chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def create_faiss_index(chunks):
    
    embeddings = embedding_model.encode(chunks)
    vectors = np.array(embeddings).astype('float32')
    
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return index

def answer_query(query, chunks, index, top_k=3):
    
    query_vec = embedding_model.encode([query]).astype('float32')
    
    D, I = index.search(query_vec, top_k)
    context = " ".join(chunks[i] for i in I[0] if i < len(chunks))

    
    model = genai.GenerativeModel("gemini-3-flash-preview")
    prompt = f"Context: {context}\n\nQuestion: {query}"
    
    response = model.generate_content(prompt)
    return response.text