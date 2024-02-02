# webscraping.io
Here's how it works:

Initialization: The script initializes the Telegram bot using the provided API token.

Command Handlers: The bot defines two command handlers:
   - `/start`: Sends a welcome message to the user and initiates the `send_updates()` function to start sending periodic updates.
   - `/help`: Provides a help message to the user explaining how the bot works.

Sending Updates Function: The `send_updates()` function continuously polls the website defined by the URL (`'https://www.ethyp.com/category/Ecommerce'`) to scrape data.
   - Inside the function, the `parser()` function is called to scrape data from the website.
   - It checks for new news items that haven't been processed before and sends them as messages to the user's chat ID.
   - The function then sleeps for 60 seconds before checking for new updates again.

Parser Function: The `parser()` function scrapes data from the website. It makes a request to the URL and parses the HTML content using BeautifulSoup.
   - It searches for all posts on the website with the class name `"company with_img g_0"`.
   - For each post, it extracts the title, address, description, and verification status.
   - If a news item has not been processed before (based on its title), it adds it to the list of new news items and marks it as processed by adding its title to the set of processed news.

Bot Polling: The bot continuously polls the Telegram API to receive messages and process updates. The `none_stop=True` parameter ensures that polling does not stop in case of errors.
