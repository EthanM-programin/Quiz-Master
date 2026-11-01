# Quiz-Master CLI

A modular, command-line Python quiz game designed to reinforce core programming syntax and support active recall study workflows.

## Features
* **Modular Architecture:** Clean separation of data (`questions.py`) and execution logic (`main.py`).
* **Input Sanitization:** Automatically handles case-insensitivity and whitespace stripping (`.strip().lower()`) for robust user experience.
* **Dynamic Scoring:** Evaluates real-time accuracy and provides performance feedback upon completion.

## Project Structure
* `questions.py` - Contains the list of question dictionaries, options, and target answers.
* `main.py` - The core game engine handling loops, user input, and score evaluation.

## Quickstart
1. Clone the repository:
   ```bash
   git clone https://github.com/EthanM-programin/Quiz-Master.git