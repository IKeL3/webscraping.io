import time
import requests
import telebot 
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6942488105:AAGVGWj0jS0dPYjKqH7QPZXgh7s80PMrTlk')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome! I will send you updates.")
    send_updates(message)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "This bot sends updates periodically. Just type /start to begin receiving updates.")

def send_updates(message):
    processed_news = set()  # Use a set to store processed news titles
    while True:
        new_news = parser(processed_news)
        for news in new_news:
            bot.send_message(message.chat.id, news, disable_web_page_preview=True)

        time.sleep(60)  # Wait for 60 seconds before checking for new updates

def parser(processed_news):
    URL = 'https://www.ethyp.com/category/Ecommerce'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    posts = soup.find_all("div", class_="company with_img g_0")
    
    new_news = []
    for post in posts:
        title = post.find("h4").text.strip()
        if title not in processed_news:
            address = post.find("div", class_="address").text.strip()
            description = post.find("div", class_="desc").text.strip()
            verified = post.find("u", class_="v").text.strip() if post.find("u", class_="v") else "Not Verified"
            news_text = f"Title: {title}\nAddress: {address}\nDescription: {description}\nVerified: {verified}"
            new_news.append(news_text)
            processed_news.add(title)  # Add the title to the set of processed news
    return new_news

bot.polling(none_stop=True)