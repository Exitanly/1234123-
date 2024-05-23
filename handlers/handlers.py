from aiogram import F, Router, types
from aiogram.types import BotCommand
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from keyboards.menu import main
router = Router()

photo = FSInputFile("source/grid_rectangle.png")

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='help', description='Правила игры'),])
    await message.reply('Привет, перед началом игры можешь изучить <a href="https://youtu.be/qAqBZF2Zj2g">правила игры в Wordle!</a>',parse_mode="HTML",reply_markup = main)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('<a href="https://youtu.be/qAqBZF2Zj2g">Правила игры в Wordle!</a>',parse_mode="HTML")
  
@router.message(lambda msg: msg.text == 'Играть')
async def add_photo(message: Message):
    await message.answer_photo(photo=photo)

@router.message(lambda msg: msg.text == 'Правила')
async def pravila(message: types.Message):
    await message.answer('<a href="https://youtu.be/qAqBZF2Zj2g">Правила игры в Wordle!</a>',parse_mode="HTML")

        
