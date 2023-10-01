# main.py

import settings
import discord
from discord.ext import commands

def run():

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():

        print(
            f'{bot.user} is ready\n'
        )

    bot.run(settings.DISCORD_TOKEN)

if __name__ == "__main__":
    run()