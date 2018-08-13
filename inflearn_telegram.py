import telegram

my_token = ''
bot = telegram.Bot(token = my_token)

chat_id = ''
message = '반갑습니다. 봇이에요'
bot.sendMessage(chat_id=chat_id, text=message)