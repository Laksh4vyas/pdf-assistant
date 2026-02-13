from utils import extract_text_from_pdf, split_text, create_faiss_index, answer_query

pdf_path = "sample.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = split_text(text)
index = create_faiss_index(chunks)

query = input("Enter your question: ")
answer = answer_query(query, chunks, index)
print("\nAnswer:\n", answer)