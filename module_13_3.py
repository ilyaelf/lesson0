from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import logging
from aiogram.enums.dice_emoji import DiceEmoji

logging.basicConfig(level=logging.DEBUG, filemode='w', filename='log.log',
                    format="%(asctime)s|%(funcName)s|%(levelname)s|%(message)s|%(pathname)s")

bot = Bot(token='')
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def all_message(message: types.Message):
    await message.answer(message.text.upper())
    await message.answer('введите /start')

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
