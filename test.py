import os
import discord
from discord import app_commands
import random
import asyncio
from dotenv import load_dotenv
from modules.model.CGPT_speech_generator import GPT_speech_generator

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
        await ctx.response.send_message('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.response.send_message(result)

@tree.command(name = "get_reminder", description = "Reminder for a person")
async def get_reminder(ctx, name: str):
    await ctx.response.defer()
    speech_gen = GPT_speech_generator()
    message = speech_gen.get_reminder_message(name)
    await ctx.followup.send(message)

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

client.run(DISCORD_API_KEY)