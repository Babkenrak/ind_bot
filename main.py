from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start',description=' Бот работать потом вац '),
        types.BotCommand(command='/help', description=' Напищну что умею вац '),
        types.BotCommand(command='/siruns', description=' Вы маи красатулачки шма '),
        types.BotCommand(command='/kyanqs', description=' Вы маи самие любимие шма '),
        types.BotCommand(command='/astvac', description=' Верь брат мой ра '),
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start (message:types.Message):
    await message.answer('Барев ахпер джан')

@dp.message_handler(commands= 'help')
async def start (message:types.Message):
    await message.reply('Я уметь помогать')

@dp.message_handler(commands= 'siruns')
async def start (message:types.Message):
    await message.reply('Ду у меня самий красивый ха')

@dp.message_handler(commands= 'kyanqs')
async def start (message:types.Message):
    await message.reply('Я тибя так люблю да')

@dp.message_handler(commands= 'astvac')
async def start (message:types.Message):
    await message.reply('Astvac qo hete')

@dp.message_handler()
async def echo(message:types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup=on_startup)