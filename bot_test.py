import sys
import variables
import telebot
import mysql.connector
from mysql.connector import errorcode

bot = telebot.TeleBot(variables.token)

try:
    db = mysql.connector.connect(
      host=variables.host,
      user=variables.user,
      passwd=variables.passwd,
      port=variables.port,
      database=variables.database
    )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    sys.exit()
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
    sys.exit()
  else:
    print(err)
    sys.exit()

cursor = db.cursor()


user_data = {}

class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ''
        

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        msg = bot.send_message(message.chat.id, "Введите имя")
        bot.register_next_step_handler(msg, process_firstname_step)

def process_firstname_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)
        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, process_lastname_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_lastname_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.last_name = message.text

        sql = "INSERT INTO users (first_name, last_name, user_id) \
                                  VALUES (%s, %s, %s)"
        val = (user.first_name, user.last_name, user_id)
        cursor.execute(sql, val)
        db.commit()

        bot.send_message(message.chat.id, "Вы зарегистрированны")
    except Exception as e:
        bot.reply_to(message, 'Ошибка регистрации')

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()
        

if __name__ == '__main__':
    bot.polling(none_stop=True)
