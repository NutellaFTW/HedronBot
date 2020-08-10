import discord
from utils import utils
import serverdatastore

async def on_join(bot, guild, member):

    autorole_name = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["autorole"]

    if autorole_name == "":
        return

    autorole = await utils.get_role(guild, autorole_name)

    if not autorole:
        return

    if autorole in member.roles:
        return

    await member.add_roles(autorole)
    
