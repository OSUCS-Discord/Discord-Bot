import discord
import functools

def check_admin(member: discord.Member):
    # change for testing OSU: 825900345565249596
    admin_role_id = 1018974719644532907
    return member.get_role(admin_role_id) is not None

# think of a way to make it a wrapper function for security purposes
# def authorization(func):
#     @functools.wraps(func)
#     def check_admin(*args, **kwds):
        