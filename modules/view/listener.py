import os
import discord
from discord import app_commands
import random
import asyncio
from dotenv import load_dotenv
# from modules.model.CGPT_speech_generator import GPT_speech_generator
load_dotenv()
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def is_valid(tag: str):
    wochentage = ['montag', 'dienstag', 'mittwoch', 'donnerstag', 'freitag', 'samstag', 'sonntag']
    return tag.lower() in wochentage

#@tree.command(name = "get_reminder", description = "Reminder for a person")
# async def get_reminder(ctx, name: str):
#     await ctx.response.defer()
#     speech_gen = GPT_speech_generator()
#     message = speech_gen.get_reminder_message(name)
#     await ctx.followup.send(message)

@tree.command(name = "pakt_schließen", description = "Verpflichte dich für dem Pakt der Zehn: Nenne deinen Namen und die Tage")
async def register_days(ctx, name: str, days: str):
    list = days.split()
    days_dict = {}
    for day in list:
        if not is_valid(day):
            await ctx.response.send_message(day + " ist kein gültiger Wochentag")
            return
        days_dict[day.lower()] = True
    test = ctx.user.id
    await ctx.response.send_message(name + " hat sich für folgende Tage verpflichtet: " + days.lower())

@tree.command(name= "missing", description= "Nenne einen Tag an dem du dem Pakt nicht beiwohnen kannst")
async def missing(ctx, day: str):
    if not is_valid(day):
            await ctx.response.send_message(day + " ist kein gültiger Wochentag")
            return
    #function mit namen return 
    await ctx.response.send_message(" hat sich für " + day + "aus dem Pakt zurückgezogen")

@tree.command(name = "mistrauensvotum", description = "Falls du der Meinung bist das ein Paktmidglied den Vertrag gebrochen hat")
async def noconfidence_start(ctx, name:str):
     print("tets")

@client.event
async def on_ready():
    await tree.sync()
    print("Arr is Ready!")

client.run(DISCORD_API_KEY)