import telegram

my_token = '612185624:AAHioMOPPjQejvv99aVYsocKlQsCISx7cE8'
bot = telegram.Bot(token = my_token)

chat_id = '341006364'
message = '반갑습니다. 봇이에요'
bot.sendMessage(chat_id=chat_id, text=message)