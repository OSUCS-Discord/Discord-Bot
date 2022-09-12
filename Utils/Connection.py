# Alex Henner
# Connection to the discord environment
import os
import discord
from dotenv import load_dotenv

# load in the .env variables for use ASK ME FOR TOKEN
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Setting intents
intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    
client.run(TOKEN)