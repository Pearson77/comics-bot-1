from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from comics import get_comics_list


def create_choice_keyboard():
    """
    Создаём разметку клавиатуры для выбора комикса
    """
    markup = InlineKeyboardMarkup(row_width=1)
    comics_lis: list[str] = get_comics_list()

    for comics in comics_lis:
        markup.add(InlineKeyboardButton(text=comics, callback_data=f"to-comics:{comics}"))

    return markup


def create_pages_keyboard(current_page: int, pages_count: int, comics: str):
    """
    Создаём разметку клавиатуры для страницы комикса
    """
    markup = InlineKeyboardMarkup()
    buttons = []

    if current_page > 1:
        data = f"to-page:{current_page - 1}:{comics}"
        buttons.append(InlineKeyboardButton(text="назад", callback_data=data))

    buttons.append(InlineKeyboardButton(text=f"{current_page}/{pages_count}", callback_data="empty"))

    if current_page != pages_count:
        data = f"to-page:{current_page + 1}:{comics}"
        buttons.append(InlineKeyboardButton(text="вперёд", callback_data=data))

    markup.add(*buttons)
    markup.add(InlineKeyboardButton(text="в начало", callback_data="to-home"))

    return markup
