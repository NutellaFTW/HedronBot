import discord
from utils import utils
import serverdatastore

async def command(bot, guild, message, command, args):
    
    if not ("administrator", True) in message.author.guild_permissions:
        return

    datastore = serverdatastore.jsonDatastore
    prefix = datastore["servers"][f"{guild.id}"]["prefix"]
    
    if len(args) == 0:
        await utils.create_embed("Error.", f"Usage: {prefix}setauditlog <#audit_log_channel>", discord.Colour.red(), message.channel)
        return

    audit_log_channel_id = args[0].replace("<", "").replace(">", "").replace("#", "")

    if not utils.represents_int(audit_log_channel_id):
        await utils.create_embed("Error.", f"Invalid Channel.", discord.Colour.red(), message.channel)
        return

    audit_log_channel = guild.get_channel(int(audit_log_channel_id))

    if not audit_log_channel:
        await utils.create_embed("Error.", f"Channel not found.", discord.Colour.red(), message.channel)
        return

    channel_name = audit_log_channel.name

    datastore["servers"][f"{guild.id}"]["audit_log_channel"] = channel_name 
    serverdatastore.writeServersJson(datastore)

    await utils.create_embed("Success!", f"Successfully changed the server audit-log to {audit_log_channel.mention}.", discord.Colour.green(), message.channel)

    

