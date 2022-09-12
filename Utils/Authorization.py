import discord

def check_admin(member: discord.Member):
    return member.get_role(825900345565249596) is not None