# OpenAI Assistant CLI Chatbot

This repository demonstrates how to integrate the OpenAI API to create a command-line interface (CLI) chatbot using Python. The chatbot utilizes the OpenAI assistant to provide responses based on user prompts.

## Setup

### Prerequisites

- Python installed on your system
- OpenAI API key

### Installation

1. Clone the repository:

```bash
   git clone https://github.com/ketanvelip/openai_assistants_cli_chatbot.git
   cd openai_assistants_cli_chatbot
```

2. Create and activate a virtual environment:

```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
    pip install -r requirements.txt
    Set up your OpenAI API key:
```

4. Create a .env file in the root directory:
```makefile
    OPENAI_API_KEY=your-openai-api-key
```

5. Run the chatbot:

```bash
python main.py
```
