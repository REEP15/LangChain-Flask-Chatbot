from flask import Flask, request, jsonify
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

app = Flask(__name__)

url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)
retriever = vector_store.as_retriever()

chat_model = ChatOpenAI(model_name="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=chat_model, retriever=retriever)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("query")
    if not user_input:
        return jsonify({"error": "Query parameter is required"}), 400
    response = qa_chain.run(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
