# LangChain Flask Chatbot

This is a simple Flask-based chatbot that extracts data from a website, processes it with LangChain, and provides responses using OpenAI's GPT-4 model.

## Features
- Scrapes data from a given URL
- Creates embeddings and stores them in a FAISS vector database
- Uses GPT-4 for generating responses
- Provides a REST API for chat interactions

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up OpenAI API key:
   ```sh
   export OPENAI_API_KEY="your-api-key"
   ```
4. Run the Flask app:
   ```sh
   python app.py
   ```

## Usage
Make a POST request to `/chat` with JSON payload:
```json
{
  "query": "What courses are available?"
}
```