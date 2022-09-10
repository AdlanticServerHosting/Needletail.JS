import os

from rich.prompt import Confirm
from time import sleep
from urllib.request import urlopen

from rich.progress import wrap_file

os.system("clear")

if Confirm.ask("Autofix isn't installed. Install it?"):
  response = urlopen("https://en.wikipedia.org/wiki/List_of_Hindi_songs_recorded_by_Asha_Bhosle")
  size = int(response.headers["Content-Length"])

  with wrap_file(response, size) as file:
      for line in file:
          print(line, end="")
          sleep(0.1)
