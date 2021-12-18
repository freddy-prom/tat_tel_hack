import config
import handlers
from loader import dp, bot
from aiogram.utils import executor


async def on_shutdown(dispatcher):
    print("goodbye!")


async def on_startup(dispatcher):
    await bot.delete_webhook()
    print("started!")


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp, on_startup=on_startup, on_shutdown=on_shutdown)
    # executor.start_webhook(
    #     dispatcher=dp, webhook_path=config.WEBHOOK_PATH,
    #     on_startup=on_startup, on_shutdown=on_shutdown,
    #     host=config.WEBAPP_HOST, port=config.WEBAPP_PORT)
