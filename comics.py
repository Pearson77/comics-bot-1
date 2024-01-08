import json


def get_page_by_number(comics: str, page: int):
    """Получение картинки комикса по номеру"""
    return open(f"comics images/{comics}/{page}.jpg", 'rb')


def get_comics_len(comics: str):
    """Получение длины комикса по названию"""
    with open("comics images/lengths.json", encoding="utf-8") as file:
        comics_lengths: dict = json.load(file)
    return comics_lengths[comics]


def get_comics_list():
    """Получение списка доступных комиксов"""
    with open("comics images/lengths.json", encoding="utf-8") as file:
        comics_lengths: dict = json.load(file)
    return comics_lengths.keys()
