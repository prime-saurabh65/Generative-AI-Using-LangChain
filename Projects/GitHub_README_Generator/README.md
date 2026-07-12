# GitHub README Generator

An AI-powered application that generates professional GitHub README files from simple project details. Built using LangChain, Google's Gemini model, and Streamlit, the application helps developers create well-structured documentation without writing Markdown manually.

---

## Features

- Generate professional README files using Google Gemini
- Multiple README generation styles
  - Professional
  - Modern
  - Minimal
- Live Markdown preview
- View generated Markdown source
- Download generated README as a `.md` file
- Clean and responsive Streamlit interface
- Powered by LangChain prompt templates and chains

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- Python Dotenv

---

## Project Structure

```text
GitHub_README_Generator/
│
├── app.py                  # Streamlit application
├── chains.py               # LangChain chain configuration
├── prompts.py              # Prompt templates
├── utils.py                # Utility functions
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── assets/
└── screenshots/
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/GenAI-Using-LangChain.git
```

Navigate to the project directory.

```bash
cd GenAI-Using-LangChain/Projects/GitHub_README_Generator
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the project directory.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

You can obtain a free API key from Google AI Studio.

---

## Run the Application

```bash
streamlit run app.py
```

The application will be available at

```
http://localhost:8501
```

---

## How It Works

1. Enter project details.
2. Select a README style.
3. LangChain formats the prompt.
4. Gemini generates a complete README.
5. Preview the output.
6. Copy or download the generated Markdown.

---

## Current Features

- Professional README generation
- Markdown rendering
- Markdown source viewer
- README download
- Gemini integration through LangChain
- PromptTemplate-based prompting

---

## Planned Improvements

- Repository URL analysis
- Automatic tech stack detection
- GitHub badge generation
- Existing README improvement
- Folder upload support
- Repository documentation assistant

---

## Screenshots

Screenshots will be added here.

---

## License

This project is licensed under the MIT License.

---

## Author

**Saurabh Shivam**

MCA (AI & IoT), NIT Patna

GitHub: https://github.com/prime-saurabh65