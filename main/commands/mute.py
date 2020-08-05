import discord
from discord.utils import get
from datetime import datetime
import serverdatastore
import asyncio

async def command(bot, guild, message, command, args):

    if not ("kick_members", True) in message.author.guild_permissions:
        return

    muted_role = get(guild.roles, name="Muted")

    if not muted_role:
        permissions = discord.Permissions(send_messages=False)
        muted_role = await guild.create_role(name="Muted", permissions=permissions)

    prefix = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["prefix"]

    if (len(args) == 0):
        embed = discord.Embed(title="Error.", description=f"Usage: {prefix}mute <@user> (optional-time-seconds, 5s, 5m, 5h, 5d)", colour=discord.Colour.red())
        embed.set_footer(text="Made by Lucas")
        embed.timestamp = datetime.utcnow()
        await message.channel.send(embed=embed)
        return

    user_id = args[0].replace("<", "").replace(">", "").replace("@!", "")

    if not represents_int(user_id):
        embed = discord.Embed(title="Error.", description=f"Invalid User.", colour=discord.Colour.red())
        embed.set_footer(text="Made by Lucas")
        embed.timestamp = datetime.utcnow()
        await message.channel.send(embed=embed)
        return

    user = guild.get_member(int(user_id))

    if not user:
        embed = discord.Embed(title="Error.", description=f"User not found.", colour=discord.Colour.red())
        embed.set_footer(text="Made by Lucas")
        embed.timestamp = datetime.utcnow()
        await message.channel.send(embed=embed)
        return

    if muted_role in user.roles:
        embed = discord.Embed(title="Success!", description=f"Unmuted {args[0]}!", colour=discord.Colour.green())
        embed.set_footer(text="Made by Lucas")
        embed.timestamp = datetime.utcnow()
        await message.channel.send(embed=embed)
        await user.remove_roles(muted_role)
        return

    if (len(args) == 2):
        time = args[1]
        if not valid_time(time):
            embed = discord.Embed(title="Error.", description=f"Invalid Time", colour=discord.Colour.red())
            embed.set_footer(text="Made by Lucas")
            embed.timestamp = datetime.utcnow()
            await message.channel.send(embed=embed)
            return
        time_seconds = get_seconds(time)
        print(time_seconds)
        await user.add_roles(muted_role)
        embed = discord.Embed(title="Success!", description=f"Muted {args[0]} for {time}!", colour=discord.Colour.green())
        embed.set_footer(text="Made by Lucas")
        embed.timestamp = datetime.utcnow()
        await message.channel.send(embed=embed)
        await asyncio.sleep(time_seconds)
        if muted_role in user.roles:
            await user.remove_roles(muted_role)
    else:
        await user.add_roles(muted_role)
        embed = discord.Embed(title="Success!", description=f"Muted {args[0]}!", colour=discord.Colour.green())
        embed.set_footer(text="Made by Lucas")
        embed.timestamp = datetime.utcnow()
        await message.channel.send(embed=embed)

seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}

def valid_time(string):
    units = string[-1]
    time = string[:-1]
    if units in seconds_per_unit and represents_int(time):
        return True
    else:
        return False

def get_seconds(string):
    return int(string[:-1]) * seconds_per_unit[string[-1]]

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
