import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import config
from database import models, database
from aiogram.contrib.fsm_storage.files import JSONStorage
from loguru import logger

loop = asyncio.get_event_loop()

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML, loop=loop)
storage = JSONStorage("states.json")
dp = Dispatcher(bot, storage=storage)

models.Base.metadata.create_all(bind=database.engine)

log = logger
log.add("log.log", level="DEBUG", rotation="500 MB")
log.info("Start")
