import telebot
import random
bot =telebot.TeleBot("1831140106:AAE-VbiKeG27yvg1XdQHM3iw7GEWdyYVSZ8")

@bot.message_handler(commands=['start'])
def say_welcome(message):
    bot.send_message(message.chat.id,"سلام خوش اومدی صفا آوردی") 

@bot.message_handler(commands=['help'])
def komak(message):
    bot.send_message(message.chat.id,"من برای کمک به شما آماده هستم")


buttons =telebot.types.ReplyKeyboardMarkup(row_width=2)
btn1 =telebot.types.KeyboardButton('🎬فیلم')
btn2 =telebot.types.KeyboardButton('🎧موسیقی')
btn3 =telebot.types.KeyboardButton('📷عکس')
btn4 =telebot.types.KeyboardButton('بازی جدید')
buttons.add(btn1,btn2,btn3,btn4)

@bot.message_handler(commands=['download'])
def mydownload(message):
    bot.send_message(message.chat.id," چی دوست داری برات بیارم؟",reply_markup=buttons)

@bot.message_handler(commands=['newgame'])
def newgame1(message):
    bot.send_message(message.chat.id," این ربات بازی حدس عدد است",reply_markup=buttons)

def rand():
    my_guess = random.randint(0, 30)
    return my_guess

@bot.message_handler(func=lambda message:True)
def send_normal_message(message):
    global my_guess
    if message.text == 'بازی جدید':
        bot.send_message(message.chat.id, "ببینم میتونی عددی که من توی ذهنم بین 0 و 30 در نظر گرفتم و حدس بزنی یا نه :")
        my_guess = rand()
    if message.text.isnumeric():
        user_guess = int(message.text)
        if user_guess == my_guess:
            bot.reply_to(message, "نِه باریکلا درست گفتی ✌")
            bot.reply_to(message, "برای بازی دوباره روی بازی جدید بزن")
        elif user_guess < my_guess:
            bot.reply_to(message, "برو بالاتر")
        elif user_guess > my_guess:
            bot.reply_to(message, "بیا پایین تر")

    if message.text =="سلام":
        bot.reply_to(message," علیک  سلام")

    elif message.text =="خوبی":
         bot.reply_to(message," نه تو خوبی ")

    elif message.text =="چه خبر؟":
         bot.reply_to(message,"سلامتی رهبر ")

    # elif message.text =="چی پوشیدی؟":
    #     photo =open("zahra.jpg","rb")
    #     bot.send_photo(message.chat.id,photo)    
    

bot.polling()