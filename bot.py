# Main bot code
from Utils.Connection import Bot
import discord
from Utils.Authorization import check_admin
from Utils.Channels import create_channels


def main():
    # change for testing OSU: 825889370636681227
    guild_id = 1018973191928025188
    
    
    client = Bot(guild_id)
    tree = client.get_tree()
    
    # interaction using slash command with the name add_new_channel
    @tree.command(name = "add_new_channel", description="Adds a new channel with roles", guild= discord.Object(id = client.get_guild_id()))
    async def role(interaction: discord.Interaction, name: str):
        if check_admin(interaction.user):
            new_role = await client.add_role(name)
            await create_channels(interaction, name, new_role)
            await interaction.response.send_message(f'New role created: {name}!')
        else:
            await interaction.response.send_message("You do not have authorization for this command")
    
    client.start_bot()
    
if __name__ == "__main__":
    main()