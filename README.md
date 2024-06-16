# use-tools
A simple project for enabling LLM agents to use tools.


### Prerequisites

#### Environment Setup
1. **Install Anaconda:**  
   Download Anaconda from [https://www.anaconda.com/](https://www.anaconda.com/).

2. **Create a Virtual Environment:**
   ```bash
   conda create -n agent_env python=3.11 pip
   ```
   
3. **Activate the Virtual Environment:**
   ```bash
   conda activate agent_env
   ```

### Clone and Navigate to the Repository
1. **Clone the Repo:**
   ```bash
   git clone https://github.com/john-adeojo/use-tools.git
   ```
2. **Navigate to the Repo:**
   ```bash
   cd /path/to/your-repo/use-tools
   ```

3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

### Configure API Keys for use with OpenAI
1. **Open the `config.yaml`:**
   ```bash
   nano config.yaml
   ```
   - **OpenAI API Key:** Get it from [https://openai.com/](https://openai.com/)


## If you want to work with Ollama

### Setup Ollama Server
1. **Download Ollama:**
   Download [https://ollama.com/download](https://ollama.com/download)

2. **Download an Ollama Model:**
   ```bash
   curl http://localhost:11434/api/pull -d "{\"name\": \"llama3:instruct\"}"
   ```
Ollama [API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md#list-local-models)

3. Navigate to the bottom of the `agent.py` script and uncomment the Ollama arguments and comment out the OpenAI arguments. 

### Run Your Query In Shell
```bash
python -m agents.agent
```
Then enter your query.

