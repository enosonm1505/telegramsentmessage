import requests
import time

base_url = "https://api.telegram.org/bot5124614020:AAEySd3wXhD4XK8m-vLk_1SSh2aRs_oOJ0A/sendDocument"

my_file = open("vuln.txt", "rb")

parameters = {
    "chat_id" : "@alertssidsix",
    "caption" : "here is another document for you"
}


files = {
    "document" : my_file
}

resp = requests.get(base_url, data = parameters, files=files)
print(resp.text)
