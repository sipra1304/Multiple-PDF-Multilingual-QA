# Multiple-PDF-Multilingual-QA
Using Google Gemini Pro

This is a simple web application built using Streamlit for extracting text from PDF files, processing them using AI models for question answering, and displaying the answers interactively.

## 🚀 Features

- **PDF Upload**: Upload multiple PDF files to extract text for analysis.
- **Question Input**: Enter a question based on the extracted text from PDFs.
- **Multilingual Support**: Supports input and output in multiple languages including English, Hindi, French, and Spanish.
- **AI-driven Answering**: Uses AI models (Google Generative AI) to answer questions based on the context extracted from PDFs.

## 🛠️ Tech Stack

- **Streamlit**: Frontend web framework for building interactive web applications.
- **Python Libraries**:
  - PyPDF2: For extracting text from PDF files.
  - LangChain: For text processing and AI-driven question answering using Google Generative AI.
  - Google Translate API: For multilingual support in input and output text.

## 🔧 Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/pdf-question-answering-system.git
   cd pdf-question-answering-system
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your Google API key to the `.env` file:
     ```dotenv
     Google_API_Key=your_google_api_key_here
     ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

5. **Open your web browser** and go to `http://localhost:8501` to view the application.

## 🎯 Usage

1. **Upload PDFs**: Use the sidebar to upload one or more PDF files. Click the "Submit" button to extract text from these PDFs.
2. **Ask a Question**: Enter a question related to the content of the uploaded PDFs in the text input field and press Enter.
3. **View Answer**: The system will display the answer based on the question and the content extracted from the PDFs.

## 🌟 Future Improvements

- Enhance user interface with more interactive features.
- Improve error handling and robustness of text extraction and question answering.
- Implement additional AI models for comparison and better accuracy in question answering.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
