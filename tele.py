import requests
import time

base_url = "https://api.telegram.org/bot5124614020:AAEySd3wXhD4XK8m-vLk_1SSh2aRs_oOJ0A/sendDocument"

my_file = open("a.txt", "rb")

parameters = {
    "chat_id" : "@alertssidsix",
    "caption" : "jenkins testing"
}


files = {
    "document" : my_file
}

resp = requests.get(base_url, data = parameters, files=files)
print(resp.text)
