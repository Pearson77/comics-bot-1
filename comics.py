import json


def get_page_by_number(comics: str, page: int):
    return open(f"comics images/{comics}/{page}.jpg", 'rb')


def get_comics_len(comics: str):
    with open("comics images/lengths.json", encoding="utf-8") as file:
        comics_lengths: dict = json.load(file)
    return comics_lengths[comics]


def get_comics_list():
    with open("comics images/lengths.json", encoding="utf-8") as file:
        comics_lengths: dict = json.load(file)
    return comics_lengths.keys()
