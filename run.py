import os
import random
from datetime import datetime

import requests


def main():
    url = os.getenv("ADDRESS")

    temperature = 36.0 + random.randrange(0, 10) * 0.1
    data = {
        "entry.2114024087": os.getenv("ROOM"),
        "entry.1323187890": os.getenv("NAME"),
        "entry.1796196705": os.getenv("ID"),
        "entry.1311885932": str(temperature),
        "entry.650077303": os.getenv("DORMITORY"),
        "entry.590103768": "없음",
        "entry.1925003746": "예",
        "entry.538682231": "예",
    }

    response = requests.post(url, data=data, verify=False, timeout=5)
    # print(response.text)
    print("success")


if __name__ == "__main__":
    end_date = datetime.strptime(os.getenv("END"), "%Y%m%d")
    now = datetime.now()

    if now < end_date:
        main()
