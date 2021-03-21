import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token="1658135418:AAFP-RnPpoZS_UShQrZgvlUhkFwbxa027II")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message)




executor.start_polling(dp)
