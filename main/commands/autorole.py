import discord
from utils import utils
import serverdatastore

async def command(bot, guild, message, command, args):
    
    if not ("administrator", True) in message.author.guild_permissions:
        return
    
    datastore = serverdatastore.jsonDatastore

    prefix = datastore["servers"][f"{guild.id}"]["prefix"]

    if len(args) == 0:
        await utils.create_embed("Error.", f"Usage: {prefix}setautorole <@newautorole>", discord.Colour.red(), message.channel)
        return

    role_id = args[0].replace("<", "").replace(">", "").replace("@&", "")

    role = guild.get_role(int(role_id))

    if not role:
        await utils.create_embed("Error.", f"Role not found.", discord.Colour.red(), message.channel)
        return

    role_name = role.name

    datastore["servers"][f"{guild.id}"]["autorole"] = role_name

    serverdatastore.writeServersJson(datastore)

    await utils.create_embed("Success!", f"Successfully changed the server autorole to {role.mention}!", discord.Colour.green(), message.channel)
