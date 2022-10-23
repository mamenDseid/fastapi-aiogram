from aiogram import Dispatcher, Bot, types

TOKEN = "5639971870:AAHkMyROj353PnrCZhgtoxw_b-JPBqubbgk"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}")