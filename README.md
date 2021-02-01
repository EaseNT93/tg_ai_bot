# tg_ai_bot
educational project(urfu)

Language:
The program is written in Python (ver. 3.7.5) using SQL in the program code.

Functionality:
This project allows to launch a telegram bot that will connect to the created database.
The bot is a task manager allowing to add tasks and their descriptions to database, view the added records and delete them.

Commands:
/start - allows to start working with the bot. User registration with the creation of a working record in the database.
/add_task - allows to add a task and its description.
/show_task - allows to see the user tasks.
/del_task - allows to delete the selected tasks.

Database creation:
The db_creator.py file allows to create a database template required for the bot to work.

Required libraries:
MySQL-connector-python
pyTelegramBotAPI

Note about library pyTelegramBotAPI:
Despite using the name in import "TELEBOT" installing the library Telebot(pip install Telebot) 
is a mistake which leads to non-execution of the code even the correct library(pip install pyTelegramBotAPI) is installed after.
To solve the problem, remove both libraries and install the correct.