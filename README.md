# PDF Chat App with Google Gemini Pro 🚀

This app enables you to ask questions about your PDF files and receive instant answers. Just type your query, and the app will search through your PDF documents providing responses.

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

## Example Images

| File           | Screenshot 1 | Screenshot 2 |
|----------------|--------------|--------------|
| **apple.pdf**  | <img src="https://github.com/MeetShah9/ask_pdf/assets/148629466/103811ae-85fb-438d-8069-48f59a77b1ae" alt="Screenshot 1" width="500"> | <img src="https://github.com/MeetShah9/ask_pdf/assets/148629466/315aa33b-d7f7-4d72-b667-d3c56d878383" alt="Screenshot 2" width="500"> |

| File                | Screenshot 3 | Screenshot 4 |
|---------------------|--------------|--------------|
| **taxi driver.pdf** | <img src="https://github.com/MeetShah9/ask_pdf/assets/148629466/a8a48126-88ca-4e96-9f40-732d7ecca430" alt="Screenshot 3" width="500"> | <img src="https://github.com/MeetShah9/ask_pdf/assets/148629466/5d3a6be8-6a27-499d-b626-1efbaace6893" alt="Screenshot 4" width="500"> |


