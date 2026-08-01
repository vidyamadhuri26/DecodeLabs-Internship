# 🤖 AI Customer Support Agent

An AI-powered Customer Support Agent built using **Google Gemini**, **Prompt Engineering**, **Streamlit**, **RAG**, and **Guardrails**.

The application analyzes customer support emails, extracts structured information, classifies complaints, checks company policies, and detects prompt injection attempts.

---

## Features

### 📋 Information Extraction
- Extracts customer details from unstructured emails.
- Returns structured JSON output.

### 🧠 Complaint Classification
- Determines:
  - Priority
  - Department
  - Estimated SLA
  - Reason

### 📚 Company Policy (RAG)
- Uses a company policy document to generate policy-based responses.

### 🛡 Prompt Injection Detection
- Detects malicious prompt injection attempts.
- Continues processing legitimate customer requests while ignoring malicious instructions.

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Prompt Engineering
- JSON
- RAG (Document-based)
- Git & GitHub

---

## Project Structure

```
DecodeLabs-Internship/

│
├── app.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── company_policy.txt
│
├── prompts/
│   ├── extraction_prompt.txt
│   ├── classification_prompt.txt
│   ├── rag_prompt.txt
│   └── guardrails_prompt.txt
│
├── src/
│   ├── extractor.py
│   ├── classifier.py
│   ├── rag.py
│   ├── guardrails.py
│   └── gemini_client.py
│
├── sample_inputs/
├── sample_outputs/
└── screenshots/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/vidyamadhuri26/DecodeLabs-Internship.git
```

Go into the project

```bash
cd DecodeLabs-Internship
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## Sample Workflow

Customer Email

↓

Security Assessment

↓

Information Extraction

↓

Complaint Classification

↓

Company Policy Decision

---

## Screenshots

Add screenshots of the application here.

---

## Author

**Vidya Madhuri**