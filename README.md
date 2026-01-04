# AI Log Analyzer 🛡️🤖

An AI-powered security log analysis tool that ingests Wazuh JSON alerts and automatically detects suspicious activity. The system explains what happened, why it matters, and provides clear remediation recommendations using LLMs.

## 🚀 Features
- **Local Analysis**: Uses [Ollama](https://ollama.com/) to process logs locally, ensuring your data never leaves your machine.
- **Wazuh Integration**: Specifically designed to parse Wazuh-style JSON alerts.
- **Human-Readable Explanations**: Converts complex security logs into simple, actionable summaries.

## 📋 Prerequisites
1. **Python 3.10+**
2. **Ollama**: Download from [ollama.com](https://ollama.com/).
3. **Node.js & npm**: Required for running the web dashboard.

## 🛠️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/supun2001/ai-log-Analyzer.git
cd ai-log-Analyzer
```

### 2. Set up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare the AI Model
Ensure the Ollama application is running on your Mac, then pull the required model:
```bash
ollama pull llama3.2
```

## 🏃 How to Run

### 1. Terminal Analyzer
1. **Add your logs**: Place your Wazuh alerts in `attacks.json`. (Ensure it is a valid JSON array of objects).
2. **Execute the analyzer**:
   ```bash
   python main.py
   ```

### 2. Web Dashboard
The project includes a premium React-based dashboard to visualize the AI analysis.

1. **Navigate to the dashboard directory**:
   ```bash
   cd dashboard
   ```
2. **Install frontend dependencies**:
   ```bash
   npm install
   ```
3. **Start the development server**:
   ```bash
   npm run dev
   ```
4. **Access the UI**: Open [http://localhost:5173](http://localhost:5173) in your browser.


## 📁 Project Structure
- `main.py`: The core logic for reading logs and interacting with Ollama.
- `attacks.json`: Your input file containing security logs.
- `requirements.txt`: Python dependencies.

## 🛡️ Security & Privacy
This tool is configured to run **locally** by default. No logs are sent to external APIs (like OpenAI or Google) when using the Ollama configuration, making it safe for sensitive internal security data.
