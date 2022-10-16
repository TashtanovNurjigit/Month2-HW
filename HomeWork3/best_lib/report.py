import requests
from datetime import date


def make_report(url: str):
    my_responce = requests.get(url)
    with open('reports.txt', mode='a+') as file:
        file.write(f'{str(date.today())} {url} {my_responce.status_code}\n')
    return my_responce
