from dotenv import load_dotenv

import os
import discord

load_dotenv()

DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_API_KEY)