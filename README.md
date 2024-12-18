# 🎵 Taylor Swift AI Chatbot 

## Project Overview

This is an AI-powered chatbot that allows users to interact with a virtual representation of Taylor Swift, leveraging RAG (Retrieval-Augmented Generation) technology and Google's Gemini AI.

## 🌟 Features

- **AI-Powered Conversations**: Interact with an AI version of Taylor Swift
- **Retrieval-Augmented Generation**: Contextually informed responses based on song data
- **Multiple Frontends**: 
- HTML/JS web frontend

## 🛠 Tech Stack

- **Backend**:
  - Python
  - LangChain
  - Google Gemini AI
  - Chroma Vector Database
  - FastAPI 

- **Frontend**:
  - HTML/CSS/JavaScript


## 📦 Prerequisites

- Python 3.8+
- Google AI Studio API Key
- Dependencies listed in `requirements.txt`

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/tushar-badlani/Taylor-Swift-Chatbot.git
cd Taylor-Swift-Chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Google API Key:
```bash
export GOOGLE_API_KEY='your_api_key_here'
```


## 🖥 Running the Application

#### FastAPI Backend
```bash
uvicorn app.main:app --reload
```

### Frontend

Open `index.html` in your browser or serve it using a local server.

## 🔧 Configuration

- Modify `system_prompt` in the code to adjust the chatbot's personality
- Customize `temperature` in Gemini configuration for response creativity
- Adjust vector search parameters in retriever configuration

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [Google Gemini](https://ai.google/)
- [Gradio](https://www.gradio.app/)
- [Dataset - adashofdata](https://github.com/adashofdata/taylor_swift_data)

## 🎤 Disclaimer

This is an AI representation and not the real Taylor Swift. Created for entertainment and educational purposes.

---
