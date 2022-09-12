# Main bot code
from Utils.Connection import Bot
import discord

def main():
    client = Bot(825889370636681227)
    tree = client.get_tree()
    
    @tree.command(name = "test", description="testing", guild= discord.Object(id = client.get_guild_id()))
    async def self(interaction: discord.Interaction, name: str):
        await interaction.response.send_message(f'Hello {name}!')
    
    client.start_bot()
    
if __name__ == "__main__":
    main()