from utils import utils
import serverdatastore
import discord

async def command(bot, guild, message, command, args):
    if not ("administrator", True) in message.author.guild_permissions:
        return
    datastore = serverdatastore.jsonDatastore
    prefix = datastore["servers"][f"{guild.id}"]["prefix"]
    if len(args) == 0:
        await utils.create_embed("Error.", f"Usage: {prefix}setwelcomemessage <new_welcome_message>", discord.Colour.red(), message.channel)
        return
    new_message = " ".join(args)
    datastore["servers"][f"{guild.id}"]["welcome_message"] = new_message 
    serverdatastore.writeServersJson(datastore)
    await utils.create_embed("Success!", f"Successfully changed the server welcome message to '{new_message}'!", discord.Colour.green(), message.channel)


