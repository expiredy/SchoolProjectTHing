import requests
import threading

path = "http://483572c62091.ngrok.io/home"

response = requests.get(path)
print(response)

while True:
    pass