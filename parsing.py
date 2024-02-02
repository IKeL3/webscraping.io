import requests
from bs4 import BeautifulSoup

URL = 'https://www.ethyp.com/category/Ecommerce'

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

posts = soup.find_all("div", class_="company with_img g_0")

for post in posts:
    title = post.find("h4").text.strip()
    address = post.find("div", class_="address").text.strip()
    description = post.find("div", class_="desc").text.strip()
    verified = post.find("u", class_="v").text.strip() if post.find("u", class_="v") else "Not Verified"
   

    print("Title:", title)
    print("Address:", address)
    print("Description:", description)
    print("Verified:", verified)
    
    print("\n")
