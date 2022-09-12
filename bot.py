# Main bot code
from Utils.Connection import Bot
import discord

def main():
    # change for testing
    guild_id = 825889370636681227
    
    client = Bot(guild_id)
    tree = client.get_tree()
    
    @tree.command(name = "add_new_channel", description="Adds a new channel with roles", guild= discord.Object(id = client.get_guild_id()))
    async def role(interaction: discord.Interaction, name: str):
        await client.add_role(name)
        await interaction.response.send_message(f'New role created: {name}!')
    
    client.start_bot()
    
if __name__ == "__main__":
    main()