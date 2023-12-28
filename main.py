from telebot import TeleBot, types
from keyboard import create_choice_keyboard, create_pages_keyboard
from comics import *
import config

bot = TeleBot(token=config.TOKEN)


@bot.message_handler(commands=['start', 'comics'])
def send_comics_choice(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Выберите комикс, который хотите прочесть:",
        reply_markup=create_choice_keyboard()
    )


@bot.callback_query_handler(lambda call: call.data.split(':')[0] == "to-page")
def return_page_by_number(callback: types.CallbackQuery):
    page, comics_name = callback.data.split(':')[1:]
    bot.edit_message_media(
        message_id=callback.message.id,
        chat_id=callback.message.chat.id,
        media=types.InputMediaPhoto(
            media=get_page_by_number(comics=comics_name, page=page)
        ),
        reply_markup=create_pages_keyboard(
            current_page=int(page),
            pages_count=get_comics_len(comics_name),
            comics=comics_name
        )
    )
    bot.answer_callback_query(callback.id)


@bot.callback_query_handler(lambda call: call.data.split(':')[0] == "to-comics")
def return_first_page_of_comics(callback: types.CallbackQuery):
    comics_name = callback.data.split(':')[1]
    bot.send_photo(
        chat_id=callback.message.chat.id,
        photo=get_page_by_number(comics=comics_name, page=1),
        reply_markup=create_pages_keyboard(
            current_page=1,
            pages_count=get_comics_len(comics_name),
            comics=comics_name
        )
    )
    bot.delete_message(message_id=callback.message.id, chat_id=callback.message.chat.id)


@bot.callback_query_handler(lambda call: call.data == "to-home")
def return_comics_choice_by_button(callback: types.CallbackQuery):
    bot.delete_message(
        message_id=callback.message.id,
        chat_id=callback.message.chat.id,
    )
    send_comics_choice(message=callback.message)
    bot.answer_callback_query(callback.id)


if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
