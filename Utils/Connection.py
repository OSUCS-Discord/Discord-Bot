# Alex Henner
# Connection to the discord environment
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import emoji

class Bot(discord.Client):
    global intents
    intents = discord.Intents.default()
    intents.message_content = True
    
    def __init__(self, guild_id: int, roles_channel_id: int) -> None:
        super().__init__(intents=intents)
        self._TOKEN = self._grab_token()
        self._synced = False
        self._guild_id = guild_id
        self._tree = app_commands.CommandTree(self)
        self._roles_channel_id = roles_channel_id
        
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
        for guild in self.guilds:
            if guild.id == self._guild_id:
                print(f'Connected to the guild {guild.name}')
                
    async def on_raw_reaction_add(self, reaction_event: discord.RawReactionActionEvent):
        try:
            message = await self.get_guild(self._guild_id).get_channel_or_thread(self._roles_channel_id).fetch_message(reaction_event.message_id)
            # print(message.content, reaction_event.emoji, reaction_event.member.name)
            role = await self._grab_role_from_emoji(message, reaction_event.emoji)
            if role is not None:
                await reaction_event.member.add_roles(role)
            
        except discord.NotFound:
            return
        
    async def on_raw_reaction_remove(self, reaction_event: discord.RawReactionActionEvent):
        try:
            message = await self.get_guild(self._guild_id).get_channel_or_thread(self._roles_channel_id).fetch_message(reaction_event.message_id)
            # print(message.content, reaction_event.emoji, reaction_event.member.name)
            role = await self._grab_role_from_emoji(message, reaction_event.emoji)
            
            if role is not None:
                member = await self.get_guild(self._guild_id).fetch_member(reaction_event.user_id)
                await member.remove_roles(role)
            
        except discord.NotFound:
            return
        
    async def _grab_role_from_name(self, role_name: str):
        roles = await self.get_guild(self.get_guild_id()).fetch_roles()
        
        for role in roles:
            if role.name == role_name:
                return role
        
        
    async def _grab_role_from_emoji(self, messages: discord.Message, current_emoji: str):
        for message in messages.content.splitlines():
            message = message.split()
            if message[0] == emoji.emojize(current_emoji.name):
                return await self._grab_role_from_name(message[1][1:])
            
    async def add_role(self, role_name: str) -> None:
        guild = self.get_guild(self.get_guild_id())
        return await guild.create_role(name=role_name)
        
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