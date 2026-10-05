# Jarvis Voice Assistant

A Python-based voice assistant that listens to spoken commands, performs web actions, plays music, fetches news, and uses AI to generate responses.

## Features

* Voice command recognition using SpeechRecognition
* Text-to-speech responses using gTTS
* Wake-word detection using `jarvis`
* Open popular websites:

  * Google
  * YouTube
  * Facebook
  * LinkedIn
* Play songs on YouTube using `pywhatkit`
* Fetch technology news using NewsAPI
* AI-powered responses using OpenAI
* Audio playback using Pygame
* Environment variables for securely managing API keys
* Modular music library for custom song mappings

## Technologies Used

* **Python**
* **SpeechRecognition**
* **gTTS**
* **PyWhatKit**
* **Requests**
* **Pygame**
* **OpenAI API**
* **NewsAPI**
* **python-dotenv**
* **PyAudio**

## Project Structure

```text
Jarvis-Voice-Assistant/
│
├── main.py
├── musicLibrary.py
├── test_voice.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

The basic workflow of Jarvis is:

```text
User speaks
     ↓
Speech Recognition
     ↓
Command Processing
     ↓
Identify the requested action
     ↓
Perform action / API request
     ↓
Generate response
     ↓
Text-to-Speech
     ↓
Jarvis speaks the response
```

## Requirements

Before running the project, make sure you have:

* Python 3.13 or compatible Python version
* A working microphone
* Internet connection
* Git
* Required Python packages
* OpenAI API key
* NewsAPI key

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Bharat033/Jarvis-Voice-Assistant.git
```

Move into the project directory:

```bash
cd Jarvis-Voice-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

This project uses environment variables to keep API keys separate from the source code.

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_news_api_key
```

**Important:** Never upload your `.env` file or API keys to GitHub.

The `.gitignore` file is configured to prevent `.env` from being committed.

## Running the Project

After activating the virtual environment and installing the dependencies, run:

```bash
python main.py
```

Allow microphone access if requested.

Then use the wake word:

```text
Jarvis
```

You can then give supported voice commands.

## Example Commands

### Open Websites

```text
Jarvis, open Google
```

```text
Jarvis, open YouTube
```

```text
Jarvis, ope
```
