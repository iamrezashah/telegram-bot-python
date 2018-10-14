# ---------------
# translation bot
# ---------------
from flask import Flask, request
import telepot
import urllib3
from mtranslate import translate

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "2"
bot = telepot.Bot(<TOKEN>)
bot.setWebhook("https://YOUR_USERNAME_IN_PYTHONANYWHERE.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)
@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    text = update["message"]["text"]
    content_type, chat_type, chat_id = telepot.glance(update["message"])
    
    translation = translate(text, 'fa', 'auto')  # translate to farsi (persian) language
    bot.sendMessage(chat_id, translation)
    
    return "OK"
