# Language Translator

This is a simple language translator application using Google Translate API and Tkinter GUI.

## Features

- Translate text between various languages supported by Google Translate.
- Integrated audio playback of translated text using gTTS library.
- User-friendly graphical interface with Tkinter.

## Getting Started

### Prerequisites

- Python 3.x
- Install dependencies:
  ```bash
  pip install -r requirements.txt

## Usage
Clone the repository:

```bash

git clone https://github.com/SimranRojia/language_translator.git
cd language_translator
```
Run the application:

```bash

python gui/main.py
```
Enter text, select the destination language, and click "Translate".

### Directory Structure

language_translator/
│
├── translator/
│   ├── __init__.py
│   └── translator.py
│
├── gui/
│   ├── __init__.py
│   └── main.py
│
├── README.md
└── requirements.txt

### Dependencies
googletrans==4.0.0rc1

### Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.