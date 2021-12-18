from aiogram.utils.exceptions import TelegramAPIError, MessageNotModified, BotBlocked
from loader import dp, log
from aiogram import types


@dp.errors_handler()
async def errors_handler(update: types.update.Update, exception: Exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    """

    if isinstance(exception, MessageNotModified):
        return True

    if isinstance(exception, BotBlocked):
        return True

    #  MUST BE THE  LAST CONDITION (ЭТО УСЛОВИЕ ВСЕГДА ДОЛЖНО БЫТЬ В КОНЦЕ)
    if isinstance(exception, TelegramAPIError):
        log.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    # At least you have tried.
    log.exception(f'Update: {update} \n{exception}')
