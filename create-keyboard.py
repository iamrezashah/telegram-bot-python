#!/usr/bin/python3.6
import telepot
import time
import urllib3
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# this bot is created and run in "www.pythonanywhere.com"
# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

bot = telepot.Bot(<TOKEN>)    # token as a string

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    
    if msg['text'] == '/start':
        bot.sendMessage(chat_id, "خوش آمدید\n ربات تست من")
    elif msg['text'] == '/info':
        bot.sendMessage(chat_id, 'my name is phika\ninstagram:\t@Phika.ir\ntelegram:\t@Phika')
    elif msg['text'] == '/keyboard':
        # to create keyboard
        row1 = [KeyboardButton(text = '0, 0'), KeyboardButton(text = '0, 1')]
        row2 = [KeyboardButton(text = '1, 0'), KeyboardButton(text = '1, 1'), KeyboardButton(text = 'remove keyboard')]
        my_keyboard = ReplyKeyboardMarkup(keyboard=[row1, row2])
        
        # to show keyboard
        bot.sendMessage(chat_id,'keyboard has been created', reply_markup = my_keyboard)
        
    elif msg['text'] == 'remove keyboard':    
        # to remove keyboard
        bot.sendMessage(chat_id, 'keyboard has been Deleted!', reply_markup=ReplyKeyboardRemove())
    else:
        bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
