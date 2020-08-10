import discord
from utils import utils
from profanity_check import predict_prob
import serverdatastore
from discord.utils import get
import asyncio

swears = []

async def on_message(bot, guild, message):

    if not swears:
        init_words()

    original_text = message.content

    staff_role = await utils.get_role(guild, "Staff")

    if staff_role in message.author.roles:
        return

    text = parse_message(original_text)

    profanity_threshold = 0.7
    profanity_probability = predict_prob([text])[0]

    if profanity_probability <= profanity_threshold and not check_swear_list(text):
        return

    await asyncio.sleep(1)

    await message.delete()

    await utils.create_embed("Warning.", f"{message.author.mention}. Your message was deemed profane.", discord.colour.Color.red(), message.channel)

    channel_name = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["audit_log_channel"]
    channel = get(guild.channels, name=channel_name, type=discord.ChannelType.text)

    if channel:
        user = message.author
        pfp_url = user.avatar_url
        embed = utils.return_embed(f"{user.name}#{user.discriminator}", f"{user.mention} has been censored.", discord.Colour.red())
        embed.add_field(name="Message", value=original_text)
        embed.set_thumbnail(url=pfp_url)
        await channel.send(embed=embed)


def parse_message(message):
    return message.replace(".", "").replace(",", "").replace("-", "")

def init_words():
    with open("events/swearWords.txt", "r") as file:
        for line in file:
            if line != "\n" and line != " " and line != "":
                swears.append(line.replace("\n", ""))

def check_swear_list(message):
    for swear in swears:
        if swear in message:
            return True
    return False
