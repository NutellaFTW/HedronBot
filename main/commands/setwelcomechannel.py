import discord
from utils import utils
import serverdatastore

async def command(bot, guild, message, command, args):
    
    if not ("administrator", True) in message.author.guild_permissions:
        return

    datastore = serverdatastore.jsonDatastore
    prefix = datastore["servers"][f"{guild.id}"]["prefix"]
    
    if len(args) == 0:
        await utils.create_embed("Error.", f"Usage: {prefix}setwelcomechannel <#welcome_channel>", discord.Colour.red(), message.channel)
        return

    welcome_channel_id = args[0].replace("<", "").replace(">", "").replace("#", "")

    if not utils.represents_int(welcome_channel_id):
        await utils.create_embed("Error.", f"Invalid Channel.", discord.Colour.red(), message.channel)
        return

    welcome_channel = guild.get_channel(int(welcome_channel_id))

    if not welcome_channel:
        await utils.create_embed("Error.", f"Channel not found.", discord.Colour.red(), message.channel)
        return

    channel_name = welcome_channel.name

    datastore["servers"][f"{guild.id}"]["welcome_channel"] = channel_name 
    serverdatastore.writeServersJson(datastore)

    await utils.create_embed("Success!", f"Successfully changed the server welcome channel to {welcome_channel.mention}.", discord.Colour.green(), message.channel)

    

