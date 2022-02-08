import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

token = os.environ.get("TOKEN")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

print(token)

client.run(token)
