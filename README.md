````markdown
# AI Email Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-green)

## 📧 Overview
The **AI Email Generator** is a web-based tool that generates professional or casual emails using **LLaMA (Large Language Model)** and **Streamlit**. Users can enter a subject, choose a tone, and optionally add details, and the model generates a complete email in seconds.

This project demonstrates the integration of **large language models** with an interactive **Python web interface**.

---

## 🛠 Features
- Generate emails in various tones: **Formal, Friendly, Persuasive, Apologetic**
- Add additional context or details to refine the email
- Streamlit-based **interactive UI**
- Easy to extend for more tones or languages

---

## 💻 Requirements
- Python 3.10+
- Streamlit
- Ollama (for local LLaMA) 

### Install dependencies (Hugging Face version):
```bash
pip install streamlit transformers torch
````

### Install Ollama (Local LLaMA version):

Follow instructions at [https://ollama.ai](https://ollama.ai) and pull the LLaMA model:

```bash
ollama pull llama3
```

---

## 🚀 Usage

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/email-generator.git
cd email-generator
```

### 2. Activate virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux / Mac
```

### 3. Run the app

#### Hugging Face version:

```bash
streamlit run email_generator.py
```

#### Ollama version:

```bash
streamlit run email_generator_ollama.py
```

* Open your browser → **[http://localhost:8501](http://localhost:8501)**
* Enter your email subject, tone, and optional details → click **Generate Email**

---

## 📂 Project Structure

```
email-generator/
│
├─ email_generator_ollama.py   # Streamlit app (Ollama version)
├─ venv/                       # Virtual environment folder (optional)
├─ requirements.txt            # Python dependencies
└─ README.md                   # Project documentation
```

---

## ⚡ How it Works

1. User inputs **email subject**, **tone**, and **optional details** in the Streamlit UI.
2. The app sends a **prompt** to the LLaMA model (local Ollama or Hugging Face API).
3. The model generates a **complete email text**.
4. Streamlit displays the generated email to the user.

---

## 🔧 Future Improvements

* Add a **“Reply to Email”** feature
* Include **tone and length sliders**
* Copy-to-clipboard and download options
* Support for multiple languages

