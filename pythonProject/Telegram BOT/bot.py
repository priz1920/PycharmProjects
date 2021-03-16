# Импортируем необходимые модули библиотеки aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Импортируем токен бота
from config import TOKEN

# Инициализируем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Создаем message_handler и объявляем там функцию ответа
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

# Создаваем обработчик команды /help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

# Делаем обработку текстового сообщения.
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

# Получать сообщения от серверов Telegram
if __name__ == '__main__':
    executor.start_polling(dp)

