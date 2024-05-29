from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline1, get_keyboard_inline_2
from database.database import initialize_db,add_user, get_user

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()


@dp.message_handler(commands= 'start')
async def start (message:types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Барев ахпер джан',reply_markup=get_keyboard_1())
    else:
        await message.answer('Барев ахпер джан', reply_markup=get_keyboard_1())


@dp.message_handler(lambda message: message.text == 'Игроки Барселоны')
async def button_1_click(message:types.Message):
    await bot.send_photo(message.chat.id, photo='https://gas-kvas.com/grafic/uploads/posts/2024-01/gas-kvas-com-p-logotipi-futbolnikh-klubov-na-prozrachnom-8.jpg', caption='Барселона', reply_markup=get_keyboard_inline1())

@dp.message_handler(lambda message: message.text == 'Следущааая клявиатура')
async def button_2_click(message:types.Message):
    await message.answer("Тут Реал",reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Игроки Реала')
async def button_3_click (message:types.Message):
    await bot.send_photo(message.chat.id, photo='https://yt3.ggpht.com/ytc/AKedOLQfNT1TujGIfKTBdvVwP8w6uZj3o5blDKh4syuK=s900-c-k-c0x00ffffff-no-rj', caption='Реал Мадрид', reply_markup=get_keyboard_inline_2())

@dp.message_handler(lambda message: message.text == 'назад клявиатура')
async def button_4_click (message:types.Message):
    await message.answer("тут кашак",reply_markup=get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
