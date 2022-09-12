# Alex Henner
# Connection to the discord environment
import os
import discord
from discord import app_commands
from dotenv import load_dotenv

class Bot(discord.Client):
        
    def __init__(self, guild_id) -> None:
        super().__init__(intents=discord.Intents.default())
        self._TOKEN = self._grab_token()
        self._synced = False
        self._guild_id = guild_id
        self._tree = app_commands.CommandTree(self)
        
    def _grab_token(self):
        # load in the .env variables for use ASK ALEX FOR TOKEN
        load_dotenv()
        return os.getenv("DISCORD_BOT_TOKEN")
    
    def get_guild_id(self):
        return self._guild_id
    
    def get_tree(self):
        return self._tree
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self._synced:
            await self._tree.sync(guild = discord.Object(id = self._guild_id))
            self._synced = True
        print(f'{self.user} has connected to Discord')
        guild = self.guilds[0]
        print(f'Connected to the guild {guild.name}')
        for channel in guild.channels:
            print(channel.name, channel.created_at)
        
    def start_bot(self):
        self.run(self._TOKEN)
        
def main():
    client = Bot(825889370636681227)
    tree = client.get_tree()
    
    @tree.command(name = "test", description="testing", guild= discord.Object(id = client.get_guild_id()))
    async def self(interaction: discord.Interaction, name: str):
        await interaction.response.send_message(f'Hello {name}!')
    
    client.start_bot()
    
if __name__ == "__main__":
    main()