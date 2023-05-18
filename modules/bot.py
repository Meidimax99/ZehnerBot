import asyncio
from modules.controller.controller import Controller
from modules.view.listener import *
from modules.view.speaker import *
from concurrent.futures import ProcessPoolExecutor


import os

CHANNEL_ID = os.getenv('CHANNEL_ID')
DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')


def main():
    executor = ProcessPoolExecutor(2)
    loop = asyncio.new_event_loop()
    speaker = loop.run_in_executor(executor, start_speaker)
    listener = loop.run_in_executor(executor, start_listener)
    loop.run_forever()
