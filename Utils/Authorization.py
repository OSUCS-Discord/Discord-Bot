import discord

def check_admin(member: discord.Member):
    # change for testing OSU: 825900345565249596
    admin_role_id = 1018974719644532907
    return member.get_role(admin_role_id) is not None