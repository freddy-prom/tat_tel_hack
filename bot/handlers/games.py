import random

from aiogram import types
from loader import dp, bot
from uuid import uuid4
from aiogram.utils.exceptions import BadRequest
from view import messages

games = [
    types.InlineQueryResultGame(id=str(uuid4()), game_short_name="find_excess"),
    types.InlineQueryResultGame(id=str(uuid4()), game_short_name="word_translation")
]


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer(messages.USE_INLINE_MODE,parse_mode="HTML", disable_web_page_preview=False)


@dp.inline_handler()
async def send_games(inline_query: types.InlineQuery):
    print(inline_query.id)
    await bot.answer_inline_query(inline_query_id=inline_query.id, results=games)


@dp.callback_query_handler(lambda callback_query: callback_query.game_short_name == "find_excess")
async def find_excess_game(query: types.CallbackQuery):
    # todo указать нормальную ссылку в будущем
    await bot.answer_callback_query(query.id, url="https://tel-hackathon.ru/find_excess/index.html")

    # todo нормально обновлять счет
    try:
        await bot.set_game_score(
            user_id=query.from_user.id, score=random.randint(1, 100),
            inline_message_id=query.inline_message_id)
    except BadRequest:
        pass


@dp.callback_query_handler(lambda callback_query: callback_query.game_short_name == "word_translation")
async def word_translation_game(query: types.CallbackQuery):
    # todo указать нормальную ссылку в будущем
    await bot.answer_callback_query(query.id, url="https://tel-hackathon.ru/word_translation.html")

    # todo нормально обновлять счет
    try:
        await bot.set_game_score(
            user_id=query.from_user.id, score=random.randint(1, 100),
            inline_message_id=query.inline_message_id)
    except BadRequest:
        pass
