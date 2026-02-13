# 📄 AI-Powered PDF Assistant (RAG System)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pdf-assistant-gom7mk8njtskcsc8asafhj.streamlit.app/)

An advanced **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions based on the content. This project uses **local embeddings** to bypass API quota limits and **Gemini 3 Flash** for high-accuracy reasoning.

---

## 🚀 Live Demo
**Click here to try it:** [PDF Assistant Live](https://pdf-assistant-gom7mk8njtskcsc8asafhj.streamlit.app/)

---

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLM:** [Google Gemini 3 Flash](https://ai.google.dev/)
* **Vector Database:** [FAISS](https://github.com/facebookresearch/faiss) (Facebook AI Similarity Search)
* **Embeddings:** [Sentence-Transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
* **PDF Processing:** [PyPDF2](https://pypdf.org/)

---

## 🧠 How It Works

1.  **Extraction:** Text is extracted from the uploaded PDF using `PyPDF2`.
2.  **Chunking:** The text is split into manageable segments (500 words each).
3.  **Local Embedding:** Chunks are converted into vector representations locally using `SentenceTransformers` (efficient & zero-cost).
4.  **Indexing:** Vectors are stored in a `FAISS` index for millisecond-speed similarity searching.
5.  **Retrieval:** When a user asks a question, the system finds the top 3 most relevant context chunks.
6.  **Generation:** The context and question are sent to **Gemini 3 Flash** to generate a grounded, factual answer.

---

## 💻 Local Setup
1. Clone the repo:
   ```bash
   git clone [https://github.com/Laksh4vyas/pdf-assistant.git](https://github.com/Laksh4vyas/pdf-assistant.git)
Install requirements:

Bash
pip install -r requirements.txt
Set up your .env:

Plaintext
GEMINI_API_KEY=your_api_key_here
Run the app:

Bash
streamlit run app.py

---

## **2. Making your GitHub "Show Something"**
If your repository page is empty, it means your `git push` didn't target the `main` branch correctly. 

**Run these 3 commands in your terminal right now:**
1. `git add .`
2. `git commit -m "Update README and project files"`
3. `git push origin main`

---

## **3. The Streamlit UI on GitHub**
To actually **show** the UI on GitHub (as a preview), you can't "embed" the working website directly into the code page, but you can do this:

### **Add a "Social Preview"**
1. Go to your Repository **Settings**.
2. Under **General**, find **Social Preview**.
3. Upload a screenshot of your working Streamlit app. Now, whenever you share the GitHub link, a beautiful preview of your UI will appear.

### **Pin the App Link**
On the right side of your GitHub repository, click the **Settings gear ⚙️** next to **About**. Paste your link `https://pdf-assistant-gom7mk8njtskcsc8asafhj.streamlit.app/` into the "Website" field. This puts the link right at the top for recruiters.

---

### **Quick Check for your Internship**
Since you are in your **6th semester**, having a RAG project that uses **Local Embeddings** mixed with **Gemini Cloud** shows you understand **hybrid architectures** (balancing cost/performance). That is a big plus for an intern!

**Would you like me to help you add a "History" feature so the app remembers