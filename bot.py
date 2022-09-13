# Main bot code
import discord
import random

from Utils.Connection import Bot
from Utils.Authorization import check_admin
from Utils.Channels import create_channels
from Utils.Messages import create_new_role_str

    
def main():
    # change for testing OSU: 825889370636681227
    GUILD_ID = 1018973191928025188
    ROLES_CHANNEL_ID = 1019066618376101888
    
    
    client = Bot(GUILD_ID, ROLES_CHANNEL_ID)
    tree = client.get_tree()
    
    # interaction using slash command with the name add_new_channel
    @tree.command(name = "add_new_channel", description="Adds a new channel with roles", guild= discord.Object(id = client.get_guild_id()))
    async def role(interaction: discord.Interaction, name: str):
        if check_admin(interaction.user):
            new_role = await client.add_role(name)
            await create_channels(interaction, name, new_role)
            roles_channel = interaction.guild.get_channel_or_thread(ROLES_CHANNEL_ID)
            await create_new_role_str(interaction.guild, roles_channel, new_role)
            await interaction.response.send_message(f'New role created: {name}!')
        else:
            await interaction.response.send_message("You do not have authorization for this command")
            
    # @tree.command(name = "read_messages", description="Testing purposes only", guild= discord.Object(id = client.get_guild_id()))
    # async def messages(interaction: discord.Interaction, name: str):
    #     if check_admin(interaction.user):
    #         role = discord.Object(id=random.randint(100,499))
    #         role.name = random.randint(100, 499)
    #         channel = 1019066618376101888
    #         await create_new_role_str(interaction.guild, interaction.guild.get_channel(channel), role)
    #         await interaction.response.send_message("read messages")
    #     else:
    #         await interaction.response.send_message("You do not have authorization for this command")
    
    client.start_bot()
    
if __name__ == "__main__":
    main()