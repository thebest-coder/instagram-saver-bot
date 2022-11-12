import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):
    # This handler will be called when user sends `/start` or `/help` command
    await message.reply("Assalomu alaykum 😊👋\n\nMen sizga instagramdan video va storylarni!\nyuklab beruvchi botman :)\n\nPowered by @thebest_coder.")
    await message.answer("⚠️Botda texnik ishlar olib borilayapti tez orada ishga tushadi")


@dp.message_handler()
async def echo(message: types.Message):
    
    await message.answer("⚠️Botda texnik ishlar olib borilayapti tez orada ishga tushadi")
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)