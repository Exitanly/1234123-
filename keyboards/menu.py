from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Играть')],
    [KeyboardButton(text='Правила')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню')