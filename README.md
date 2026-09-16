# MMN Telegram Bot

A simple and extensible Telegram bot project built with Python.

## Features

- Telegram bot structure
- Easy configuration
- Secure token management with environment variables
- Simple and maintainable Python code

## Technologies

- Python
- Telegram Bot API
- python-telegram-bot
- python-dotenv
  

## Installation

Clone the repository:

    git clone https://github.com/MMN-software/MMN-telegram-bot.git
    cd MMN-telegram-bot

Create a virtual environment:

    python -m venv venv

Activate the virtual environment.

On Windows:

    venv\Scripts\activate

On Linux or macOS:

    source venv/bin/activate

Install the dependencies:

    pip install -r requirements.txt

## Configuration

Create a `.env` file in the project root:

    BOT_TOKEN=your_telegram_bot_token

Never publish your real bot token or other sensitive information on GitHub.

## Usage

Run the bot with:

    python bot.py

## Project Structure

    MMN-telegram-bot/
    ├── bot.py
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── README.md

## License

This project is for educational and portfolio purposes.
