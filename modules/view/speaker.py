from dotenv import load_dotenv
import discord
import asyncio
from discord.ext import tasks
from ..controller import controller
from datetime import datetime
import os
load_dotenv()
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')

def start_speaker(): 
    client = MyClient(intents=discord.Intents.default())
    client.run(DISCORD_API_KEY)

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(int(CHANNEL_ID))  # channel ID goes here
        criticalTime = controller.controller.triggertime
        print("Test")
        warned = False
        while not self.is_closed():
            now = datetime.now()
            if( now.strftime("%H:%M") == criticalTime and not warned):
                await channel.send(controller.controller.get_reminder_message())
                warned = True
            if( now.strftime("%H:%M") != criticalTime and warned):
                warned = False
            await asyncio.sleep(10)  # task runs every 60 seconds

    async def proofs_missing(self):
        await self.wait_until_ready()
        

