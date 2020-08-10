import discord
from discord.utils import get
from datetime import datetime
import serverdatastore
import asyncio
from utils import utils

async def command(bot, guild, message, command, args):

    if not ("kick_members", True) in message.author.guild_permissions:
        return

    muted_role = await utils.get_role(guild, "Muted")

    prefix = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["prefix"]

    if (len(args) == 0):
        await utils.create_embed("Error.", f"Usage: {prefix}mute <@user> (optional-time-seconds, 5s, 5m, 5h, 5d)", discord.Colour.red(), message.channel)
        return

    user_id = args[0].replace("<", "").replace(">", "").replace("@!", "")

    if not utils.represents_int(user_id):
        await utils.create_embed("Error.", f"Invalid User.", discord.Colour.red(), message.channel)
        return

    user = guild.get_member(int(user_id))

    if not user:
        await utils.create_embed("Error.", f"User not found.", discord.Colour.red(), message.channel)
        return

    if muted_role in user.roles:
        await utils.create_embed("Success!", f"Unmuted {args[0]}!", discord.Colour.green(), message.channel)
        await user.remove_roles(muted_role)
        return

    channel_name = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["audit_log_channel"]
    channel = get(guild.channels, name=channel_name, type=discord.ChannelType.text)

    if (len(args) == 2):
        time = args[1]
        if not valid_time(time):
            await utils.create_embed("Error.", f"Invalid Time", discord.Colour.red(), message.channel)
            return
        time_seconds = get_seconds(time)
        print(time_seconds)

        await user.add_roles(muted_role)
        await utils.create_embed("Success!", f"Muted {args[0]} for {time}!", discord.Colour.green(), message.channel)

        if channel:
            pfp_url = user.avatar_url
            embed = utils.return_embed(f"{user.name}#{user.discriminator}", f"{user.mention} has been muted for {time}!", discord.Colour.red())
            embed.set_thumbnail(url=pfp_url)
            await channel.send(embed=embed)

        await asyncio.sleep(time_seconds)
        if muted_role in user.roles:
            await user.remove_roles(muted_role)
    else:

        await user.add_roles(muted_role)
        await utils.create_embed("Success!", f"Muted {args[0]}!", discord.Colour.green(), message.channel)

        if channel:
            pfp_url = user.avatar_url
            embed = utils.return_embed(f"{user.name}#{user.discriminator}", f"{user.mention} has been muted!", discord.Colour.red())
            embed.set_thumbnail(url=pfp_url)
            await channel.send(embed=embed)


seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}

def valid_time(string):
    units = string[-1]
    time = string[:-1]
    if units in seconds_per_unit and utils.represents_int(time):
        return True
    else:
        return False

def get_seconds(string):
    return int(string[:-1]) * seconds_per_unit[string[-1]]
