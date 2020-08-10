import discord
from datetime import datetime
import serverdatastore
from utils import utils

async def command(bot, guild, message, command, args):

    if not ("administrator", True) in message.author.guild_permissions:
        return

    datastore = serverdatastore.jsonDatastore
    prefix = datastore["servers"][f"{guild.id}"]["prefix"]

    if len(args) == 0:
        await utils.create_embed("Error.", f"Usage: {prefix}setprefix <newprefix>", discord.Colour.red(), message.channel)
        return

    newPrefix = " ".join(args)

    datastore["servers"][f"{guild.id}"]["prefix"] = newPrefix 
    serverdatastore.writeServersJson(datastore)

    await utils.create_embed("Success!", f"Successfully changed the server prefix from '{prefix}' to '{newPrefix}'.", discord.Colour.green(), message.channel)
