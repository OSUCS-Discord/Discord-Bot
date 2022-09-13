import discord
import emoji
import random

async def get_messages(guild: discord.Guild):
    # Change this for testing OSU: 879539007703371826 Roles
    channel_id = 1019066618376101888 
    channel = guild.get_channel_or_thread(channel_id)

    messages: list[discord.Message] = [message async for message in channel.history(limit=10)]
    return messages
    
    
def get_next_emoji(messages: list[discord.Message]):
    emojis = []
    for message in messages:
        for line in message.content.splitlines():
            emojis.append(line.split()[0])
            
    new_emoji = None
    potential_emojis = list(emoji.EMOJI_DATA.values())
    while new_emoji is None or new_emoji in emojis:
        new_emoji = random.choice(potential_emojis)
        
    return emoji.emojize(new_emoji["en"])[0]

async def create_new_role_str(guild: discord.Guild, channel: discord.TextChannel, role: discord.Role, category: discord.CategoryChannel):
    messages = await get_messages(guild)
    new_emoji = get_next_emoji(messages)
    message = get_next_message_id(messages)
    
    if message is None:
        message = await create_new_emoji_locations(channel, new_emoji, role)
    else:
        previous_message = message.content
        await message.edit(content=f"{previous_message}\n{new_emoji} @{role}")
    
    await message.add_reaction(new_emoji)
    
def get_next_message_id(messages: list[discord.Message]):
    next_message = None
    for message in messages:
        if message.author.id != 1018885005939834910:
            continue
        elif len(message.content.splitlines()) >= 10:
            continue
        else:
            next_message = message
            break
        
    return next_message
        

async def create_new_emoji_locations(channel: discord.TextChannel, emoji: str, role: discord.Role):
    # if there isn't space
    return await channel.send(f"{emoji} @{role.name}")

