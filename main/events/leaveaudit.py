from utils import utils
import serverdatastore
import discord
from discord.utils import get

async def on_leave(bot, guild, member):

    channel_name = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["audit_log_channel"]

    if channel_name == "":
        return

    channel = get(guild.channels, name=channel_name, type=discord.ChannelType.text)

    if not channel:
        return

    pfp_url = member.avatar_url

    embed = utils.return_embed(f"{member.name}#{member.discriminator}", f"{member.mention} has left the server!", discord.Colour.red())
    embed.set_thumbnail(url=pfp_url)

    await channel.send(embed=embed)
