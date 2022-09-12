import discord

async def create_channels(interaction: discord.Interaction, name: str, new_role: discord.Role):
    category_channel = await interaction.guild.create_category(name)
    # need to make sure @everyone permission gets turned off for view and connect
    # need to make sure all permission gets turned on for view and connect
    # need the newly created role gets turned on for view and connect
    overwrite = discord.PermissionOverwrite()
    all_roles = await interaction.guild.fetch_roles()
    for role in all_roles:
        print(role.name)
        if role.name == new_role.name or role.name == "all":
            overwrite.connect = True
            overwrite.view_channel = True
        elif role.name == "@everyone":
            overwrite.connect = False
            overwrite.view_channel = False
        else:
            continue
        await category_channel.set_permissions(role, overwrite=overwrite)
    
    