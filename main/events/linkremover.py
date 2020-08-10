import discord
import re
from utils import utils
import serverdatastore
from discord.utils import get

async def on_message(bot, guild, message):

    if ("administrator", True) in message.author.guild_permissions:
        return

    original_text = message.content

    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', original_text)

    if valid_url(urls):
        return

    await message.delete()

    await utils.create_embed("Warning.", f"{message.author.mention}. You are not allowed links.", discord.colour.Color.red(), message.channel)

    channel_name = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["audit_log_channel"]
    channel = get(guild.channels, name=channel_name, type=discord.ChannelType.text)

    if channel:
        user = message.author
        pfp_url = user.avatar_url
        embed = utils.return_embed(f"{user.name}#{user.discriminator}", f"{user.mention} has been censored for trying to post a link.", discord.Colour.red())
        embed.add_field(name="Message", value=original_text)
        embed.set_thumbnail(url=pfp_url)
        await channel.send(embed=embed)

def valid_url(urls):
    for url in urls:
        if not url.startswith("https://quantumcraft.xyz"):
            return False
    return True