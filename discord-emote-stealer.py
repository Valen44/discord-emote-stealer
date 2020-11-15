import re
import requests
import os
from pathlib import Path

with open("html.txt", "r", encoding="utf8") as f:
    html = f.read()
serverName = re.findall(r'(?<=img alt=").*?(?=")', html)
links = re.findall(r"https://cdn.discordapp.com/emojis/\d+.png", html)
filenames = re.findall(r'(?<=alt=":)\S*(?=:")', html)

directory = "".join(serverName)

Path("./{}".format(directory)).mkdir(parents=True, exist_ok=True)

for name, link in zip(filenames, links):
    r = requests.get(link)
    with open(os.path.join("./{}".format(directory), name) + ".png", "wb") as f:
        f.write(r.content)
        
print(
    "Successfully downloaded {} emotes from {} server.".format(
        len(filenames), directory
    )
)
