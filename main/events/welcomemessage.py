import discord
from utils import utils
import serverdatastore
from discord.utils import get

async def on_join(bot, guild, member):

    datastore = serverdatastore.jsonDatastore

    welcome_message = datastore["servers"][f"{guild.id}"]["welcome_message"].replace("{member}", member.mention)

    if welcome_message == "":
        return

    channel_name = datastore["servers"][f"{guild.id}"]["welcome_channel"]

    if channel_name == "":
        return

    channel = get(guild.channels, name=channel_name, type=discord.ChannelType.text)

    if not channel:
        return

    pfp_url = member.avatar_url

    embed = utils.return_embed("Welcome!", welcome_message, discord.Colour.green())
    embed.set_thumbnail(url=pfp_url)
    
    await channel.send(embed=embed)
