import discord

async def create_channels(interaction: discord.Interaction, name: str, new_role: discord.Role):
    category_channel = await interaction.guild.create_category(name)
    # need to make sure @everyone permission gets turned off for view and connect
    # need to make sure all permission gets turned on for view and connect
    # need the newly created role gets turned on for view and connect
    
    all_roles = await interaction.guild.fetch_roles()
    await update_permissions(all_roles, category_channel, new_role)
    channels = [name+'-resources', name+'-general']
    for channel in channels:
        await category_channel.create_text_channel(channel)
        
    return category_channel
    
    
async def update_permissions(roles: discord.Role, channel: discord.CategoryChannel, new_role: discord.Role):
    for role in roles:
        overwrite = discord.PermissionOverwrite()
        if role.name == new_role.name or role.name == "all":
            overwrite.connect = True
            overwrite.view_channel = True
        elif role.name == "@everyone":
            overwrite.connect = False
            overwrite.view_channel = False
        else:
            continue
        
        # print(f'Try {role.name} with {overwrite._values}')
        await channel.set_permissions(role, overwrite=overwrite)