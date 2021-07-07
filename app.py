import time
from datetime import datetime

import requests
from requests.exceptions import HTTPError

while True:
    response = requests.get("https://google.com")
    try:
        response.raise_for_status()
    except HTTPError:
        with open('file.txt', 'a') as f:
            f.write("Google server is up - {}\n".format(datetime.now()))
    else:
        with open('file.txt', 'a') as f:
            f.write("Google server is down - {}\n".format(datetime.now()))

    time.sleep(5)
