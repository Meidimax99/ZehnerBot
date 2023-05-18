from dotenv import load_dotenv
import discord
import asyncio
from discord.ext import tasks
#from ..controller import controller

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
        counter = 0
        channel = self.get_channel(int(CHANNEL_ID))  # channel ID goes here
        while not self.is_closed():
            counter += 1
            await channel.send(counter)
            await asyncio.sleep(5)  # task runs every 60 seconds


