from dotenv import load_dotenv
import discord
from discord.ext import commands
from dataclasses import dataclass
from ..controller import controller
import os

load_dotenv()
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')

description = '''Description'''
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', description=description, intents=intents)

def start_listener():
    bot.run(DISCORD_API_KEY)

# Commands here

@bot.command()
async def regChannelOnly(ctx, *choices: str):
    """Chooses between multiple choices."""
    global channelID
    print(ctx.channel.id)
    if ctx.channel.id == channelID or channelID == "":
        await ctx.send("You are in the registered channel")
    else:
    	await ctx.send("The Bot is not registered to this channel")

@bot.command()
async def test(ctx):
    await ctx.send(controller.controller.getTestText())
    
@bot.command()
async def registerToChannel(ctx):
    """Registers the bot to this specific channel."""
    print(ctx.channel.id)
    global channelID
    channelID = ctx.channel.id
    await ctx.send("Bot has been registered to this channel")
 
