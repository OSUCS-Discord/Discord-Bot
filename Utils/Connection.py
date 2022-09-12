# Alex Henner
# Connection to the discord environment
import os
import discord
from dotenv import load_dotenv

class connection:
    # I hate this, but the async function can't have self
    global _client
    _intents = discord.Intents.default()
    _client = discord.Client(intents=_intents)
        
    def __init__(self) -> None:
        self._TOKEN = self._get_token()
        
    def _get_token(self):
        # load in the .env variables for use ASK ME FOR TOKEN
        load_dotenv()
        return os.getenv("DISCORD_BOT_TOKEN")
    
    @_client.event
    async def on_ready():
        print(f'{_client.user} has connected to Discord')
    
    def run(self):
        _client.run(self._TOKEN)
        
def main():
    connect = connection()
    connect.run()
    
if __name__ == "__main__":
    main()