import discord
from utils import utils
import serverdatastore
from discord.utils import get

async def on_join(bot, guild, member):

    channel_name = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["audit_log_channel"]

    if channel_name == "":
        return

    channel = get(guild.channels, name=channel_name, type=discord.ChannelType.text)

    if not channel:
        return

    pfp_url = member.avatar_url

    embed = utils.return_embed(f"{member.name}#{member.discriminator}", f"{member.mention} has joined the server!", discord.Colour.green())
    embed.set_thumbnail(url=pfp_url)

    await channel.send(embed=embed)

