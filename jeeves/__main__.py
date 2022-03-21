#!/usr/bin/env python3

import asyncio
from os import environ

from dotenv import load_dotenv
from loguru import logger

from jeeves import Jeeves

bot = Jeeves()

load_dotenv()


async def main():
    async with bot:
        logger.info("Starting bot...")
        await bot.start(environ.get("BOT_TOKEN"))


asyncio.run(main())
