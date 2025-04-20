import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('hello!')


token = os.getenv('TOKEN')
if token is None:
  print('Error: Token is not set')
  exit()
  # exit the program if the token is not set
client.run(token)  

  

