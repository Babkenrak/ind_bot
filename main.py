from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands= 'start')
async def start (message:types.Message):
    await message.answer('Барев ахпер джан',reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Атпрафь фота ката')
async def button_1_click (message:types.Message):
    await bot.send_photo(message.chat.id, photo='https://avatars.dzeninfra.ru/get-zen_doc/4079787/pub_618567c4e588c64ad2925385_618567e910c41e5eeb4186bf/scale_1200', caption='кашара', reply_markup=get_keyboard_inline())

@dp.message_handler(lambda message: message.text == 'Следущааая клявиатура')
async def button_2_click (message:types.Message):
    await message.answer("тут сабака",reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Атпрафь фота сабаки')
async def button_3_click (message:types.Message):
    await bot.send_photo(message.chat.id, photo='https://sportishka.com/uploads/posts/2022-11/1667555715_49-sportishka-com-p-stafford-nakachennii-instagram-59.jpg', caption='сабак')

@dp.message_handler(lambda message: message.text == 'назад клявиатура')
async def button_4_click (message:types.Message):
    await message.answer("тут кашак",reply_markup=get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)