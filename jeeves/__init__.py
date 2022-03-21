from os import environ

import discord
from discord import app_commands
from dotenv import load_dotenv
from loguru import logger

from jeeves import loader


load_dotenv()


class Jeeves(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            intents=intents,
            activity=discord.Game(name="Emacs"),
            allowed_mentions=discord.AllowedMentions.none(),
        )

        self.tree = app_commands.CommandTree(self)

        mods = loader.find_mods()

        for mod in mods:
            self.tree.add_command(
                mod(), guild=discord.Object(id=int(environ.get("BOT_GUILD")))
            )

    async def on_ready(self):
        logger.info(f"Logged in as {self.user}")
        logger.info("Starting command sync...")
        await self.tree.sync(guild=discord.Object(id=int(environ.get("BOT_GUILD"))))
        logger.info("Finished command sync...")
