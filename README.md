# Typer CLI greeting app
This project is a simple command-line interface (CLI) application built with Typer.
it demonstrates how to create user-friendly CLI commands in Python using type hints and decorators.
## Features
- Built with Typer, a modern library for building CLI apps
- Accepts a user’s name as input and prints a personalized greeting
- Easy to extend with more commands in the future.
## Installation
1. Clone this repository:
    ```
    git clone https://github.com/your-username/typer-greeting-app.git
    cd typer-greeting-app
    ```
2. create a virtual environtment (optional)
    ```
    python -m venv venv
    source venv/bin/activate (on macOS/Linux)
    venv/Scripts/activate (on Windows)
    ```
3. install dependencies:
    ```
    pip install typer
    ```
## Usage
run the app with python:
    ```
    python cli.py greeting NAME
    ```
### Example:
```
python cli.py greeting Maryam
```
### Output:
hello Maryam 👋
## How It Works
- The ``` @app.command () ``` decorator registers the function greeting as a CLI command.
- The function expects one argument (name: str).
- Typer automatically handles parsing and displaying help messages.
### For example, running:
```
python cli.py --help
```
will display the automatically generated help text.
### Example help Output
```
Usage: cli.py [OPTIONS] NAME
Arguments:
NAME [required]
Options:
    --help show this message and exit
```
## Why Typer?
•	Type hints = better developer experience
•	Automatic help messages
•	Minimal boilerplate code
•	Easy to scale for larger CLI apps
## License
This project is licensed under the MIT License. Feel free to use and modify it.

