import requests
from colorama import init, fore, back

init() 

response = requests.get(
    "https://icanhazdadjoke.com/",
    headers={"Accept":"application/json"})

print(back.blue + fore.yellow + "Your dad joke: {0}".format(response.json()["joke"]))

input("Press ENTER to continue.")
