from dotenv import load_dotenv
from ..controller import controller
import os
import discord
from discord import app_commands
from typing import Union
from dotenv import load_dotenv
load_dotenv()
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def start_listener():
    client.run(DISCORD_API_KEY)


def is_valid(tag: str):
    wochentage = ['montag', 'dienstag', 'mittwoch', 'donnerstag', 'freitag', 'samstag', 'sonntag']
    return tag.lower() in wochentage


# Commands here

@tree.command(name = "reg_channel", description = "Check if this is the registered channel")
async def regChannelOnly(ctx):
    """Chooses between multiple choices."""
    global channelID
    print(ctx.channel.id)
    if ctx.channel.id == channelID or channelID == "":
        await ctx.response.send_message("You are in the registered channel")
    else:
    	await ctx.response.send_message("The Bot is not registered to this channel")

@tree.command(name = "test", description = "Test access to controller")
async def test(ctx):
    await ctx.response.send_message(controller.controller.getTestText())

@tree.command(name = "test_gpt", description = "Get message from GPT")
async def testGPT(ctx):
    await ctx.response.send_message(controller.controller.get_reminder_message(None))

@tree.command(name = "register_to_channel", description = "Register the bot to the specific channel")
async def registerToChannel(ctx):
    """Registers the bot to this specific channel."""
    print(ctx.channel.id)
    global channelID
    channelID = ctx.channel.id
    await ctx.send("Bot has been registered to this channel")

@tree.command(name = "pakt_schließen", description = "Verpflichte dich für dem Pakt der Zehn: Nenne deinen Namen und die Tage")
async def register_days(ctx, name: str, days: str):
    await ctx.response.defer()
    userid = "<@" + str(ctx.user.id) +">"

    list = days.split()
    days_dict = {}
    for day in list:
        if not is_valid(day):
            await ctx.followup.send(day + " ist kein gültiger Wochentag")
            return
        days_dict[day.lower()] = True
    message = controller.controller.get_register_message(userid, list)
    await ctx.followup.send(message)

@tree.command(name= "missing", description= "Nenne einen Tag an dem du dem Pakt nicht beiwohnen kannst")
async def missing(ctx, day: str):
    userid = ctx.user.id
    await ctx.response.defer()
    if not is_valid(day):
            await ctx.followup.send(day + " ist kein Gültiger Tag")
            return
    #function mit namen return
    message = controller.controller.get_acknowledge_off_day_message("<@" + str(userid) +">" ,day)
    await ctx.followup.send(message)

@tree.command(name = "mistrauensvotum", description = "Falls du der Meinung bist das ein Paktmidglied den Vertrag gebrochen hat")
async def noconfidence_start(ctx, name:str, day:str):

    #TODO check for valid name 
    #TODO funktion hier
    await ctx.response.defer()
    print(name)
    if not is_valid(day):
            await ctx.followup.send(day + " ist kein Gültiger Tag")
            return
    message = controller.controller.get_start_no_convidence_vote_message(name, day)
    await ctx.followup.send(message)

@tree.command(name="abstimmen", description="stimme im aktuellen mistrauensvotum ab")
@app_commands.rename(vote="stimme")
async def vote(ctx, vote: bool):
    userid = ctx.user.id
    await ctx.response.send_message(f"<@{ctx.user.id}> hat abgestimmt")
     
@tree.command(name="anwesenheits_beweis", description="Dein Anwesendheitsbeweis")
async def proof(ctx):
    userid = ctx.user.id
    await ctx.response.send_message(f"<@{userid}> hat einen Beweis eingereicht")
    


@client.event
async def on_ready():
    await tree.sync()
    print("Arr is Ready!")