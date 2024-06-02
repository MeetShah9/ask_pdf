# PDF Chat App with Google Gemini Pro 🚀

This is a Streamlit web application that allows users to interactively chat with their PDF files using Google Gemini Pro for question-answering capabilities.

## Features

- **PDF Upload:** Users can upload one or multiple PDF files.
- **Interactive Chat:** Users can ask questions about the uploaded PDF files and receive answers based on the content of the documents.
- **Google Gemini Pro Integration:** The app leverages Google's Generative AI (Gemini Pro) for advanced question-answering.

## Installation

1. Clone this repository:

```
git clone <repository-url>
cd <repository-directory>
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up your Google API key by creating a `.env` file in the root directory and adding your API key:

```
GOOGLE_API_KEY=your-api-key
```

4. Run the Streamlit app:

```
streamlit run app.py
```

## Dependencies

- streamlit
- google-generativeai
- python-dotenv
- langchain
- PyPDF2
- faiss-cpu
- langchain_google_genai


