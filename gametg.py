import telebot
bot = telebot.TeleBot ('1751291259:AAF_LGVOHFWXyizuxpezrpnykH5Cak8MK2Y')

@bot.message_handler (commands = ["Start"])
def Start(message):
	

	bot.send_game(chat_id=message.chat.id, game_short_name='tetris')


if _name_ == "_main_":

	bot.polling()