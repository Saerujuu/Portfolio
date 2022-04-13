from instabot import Bot

bot = Bot()

bot.login(username="londonhustlersclub", password="Superd0g")
image = "img/elsalgdpraisebtc.png"

bot.upload_photo(image, caption="ElSalvador's GDB grew 10.3% first time in it's history after adopting Bitcoin as "
                                "legal tender.")
