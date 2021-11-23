import requests

chat_id = -766097134
base_bot_url = "https://api.telegram.org/bot2108370487:AAGqAcpYdKwsRYWN561tvuajTeUENYz3m9c/getUpdates"
bot_message_sharing_url = "https://api.telegram.org/bot2108370487:AAGqAcpYdKwsRYWN561tvuajTeUENYz3m9c/sendMessage?chat_id=-766097134&text=Human Detection have happened"


#files = {'photo':open(r"runs\detect\exp\bus.jpg",'rb')}
bot_photo_sharing_url = "https://api.telegram.org/bot2108370487:AAGqAcpYdKwsRYWN561tvuajTeUENYz3m9c/sendPhoto?chat_id=-766097134"
bot_video_sharing_url = "https://api.telegram.org/bot2108370487:AAGqAcpYdKwsRYWN561tvuajTeUENYz3m9c/sendVideo?chat_id=-766097134"

# sending the data over telegram
def share_photo_data(files):
    requests.get(bot_message_sharing_url)
    requests.post(bot_photo_sharing_url,files=files)
    
def share_video_data(files):
    requests.get(bot_message_sharing_url)
    requests.post(bot_video_sharing_url,files=files)

#requests.post(bot_video_sharing_url,files={'video':open(r"runs\detect\\exp3\\0.mp4",'rb')})