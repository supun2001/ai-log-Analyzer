# AI Log Analyzer 🛡️🤖

An AI-powered security log analysis tool that ingests Wazuh JSON alerts and automatically detects suspicious activity. The system explains what happened, why it matters, and provides clear remediation recommendations using LLMs.

## 🚀 Features
- **Local Analysis**: Uses [Ollama](https://ollama.com/) to process logs locally, ensuring your data never leaves your machine.
- **Wazuh Integration**: Specifically designed to parse Wazuh-style JSON alerts.
- **AI Dashboard**: A premium React interface to visualize the analysis of security events.
- **Human-Readable Explanations**: Converts complex security logs into simple, actionable summaries.

## 📋 Prerequisites
1. **Python 3.10+**
2. **Ollama**: Download and install from [ollama.com](https://ollama.com/).
3. **Node.js & npm**: Required for running the web dashboard.

## 🛠️ Setup & Installation

### 1. Clone & Prepare
```bash
git clone https://github.com/supun2001/ai-log-Analyzer.git
cd ai-log-Analyzer

# Setup Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Initial Model Download (Requires Ollama running)
ollama pull llama3.2
```

### 2. Dashboard Setup
```bash
cd dashboard
npm install
cd ..
```

## 🏃 Running the Project

**Note**: This project operates in a **standalone environment** for demonstration purposes. It uses a sample Wazuh security log file (`attacks.json`) to showcase the AI's analytical capabilities without requiring a live connection to a Wazuh manager.

### Step 1: Analyze Logs (Backend)
This script processes the logs in `attacks.json` and generates the analysis for the dashboard.
```bash
# Ensure your venv is active
source venv/bin/activate
python main.py
```

### Step 2: Start Dashboard (Frontend)
Run this in a separate terminal window to view the results.
```bash
cd dashboard
npm run dev
```
Open **[http://localhost:5173](http://localhost:5173)** to see your live security analysis!

## 📁 Project Structure
- `main.py`: The core logic for reading logs and interacting with Ollama.
- `attacks.json`: Your input file containing security logs.
- `requirements.txt`: Python dependencies.
- `dashboard/`: React web interface.
- `dashboard/public/alerts.json`: The generated analysis data.

## 🛡️ Security & Privacy
This tool is configured to run **locally** by default. No logs are sent to external APIs (like OpenAI or Google) when using the Ollama configuration, making it safe for sensitive internal security data.
