import os
import discord
from discord import app_commands
from discord.ext import commands
import random
from dotenv import load_dotenv

load_dotenv()
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "roll", description = "Roll NdN dice")
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

client.run(DISCORD_API_KEY)