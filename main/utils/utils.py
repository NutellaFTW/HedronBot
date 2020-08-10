from datetime import datetime
import discord
from discord.utils import get
import asyncio

async def create_embed(title, description, colour, channel):
    embed = discord.Embed(title=title, description=description, colour=colour)
    embed.set_footer(text="Made by Lucas")
    embed.timestamp = datetime.utcnow()
    message = await channel.send(embed=embed)
    await asyncio.sleep(5)
    await message.delete()

def return_embed(title, description, colour):
    embed = discord.Embed(title=title, description=description, colour=colour)
    embed.set_footer(text="Made by Lucas")
    embed.timestamp = datetime.utcnow()
    return embed

async def get_role(guild, name):
    role = get(guild.roles, name=name)
    if not role:
        role = await guild.create_role(name=name)
    return role

def get_combined_message(args, index):
    length = len(args)
    combined = ""
    for i in range(index, length):
        combined += args[i] + " "
    return combined.strip()

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
