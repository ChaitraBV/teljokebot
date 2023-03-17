# Joke Bot

This is a simple Telegram bot that presents users with three buttons - "stupid", "fat", and "dumb" - and displays an appropriate joke when a button is clicked. The bot also tracks the number of times each button is pressed, and stores the counts on a per-user basis in a PostgreSQL database.

## Installation

To install the dependencies, run:

```sh
pip install -r requirements.txt

## Configuration
##Before running the bot, you will need to set up a Telegram bot and obtain an API token. You can do this by following the instructions in the Telegram Bot API documentation.

##Once you have obtained a token, create a .env file in the project root directory and add the following line, replacing YOUR_API_TOKEN with your actual API token:

TELEGRAM_BOT_TOKEN=YOUR_API_TOKEN


## Next, create a PostgreSQL database and add the connection details to the .env file:

DB_NAME=myproject
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost
DB_PORT=5432


## Usage
## To start the bot, run:

python manage.py runserver


##This will start the Django development server and the bot will be available at http://localhost:8000/.
##To view the user call counts, go to 

http://localhost:8000/user_calls/.

