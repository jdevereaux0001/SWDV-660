import requests
from colorama import init, fore, back

init() 

response = requests.get(
    "https://icanhazdadjoke.com/",
    headers={"Accept":"application/json"})

print(Back.BLUE + Fore.YELLOW + "Your dad joke: {0}".format(response.json()["joke"]))

input("Press ENTER to continue.")
