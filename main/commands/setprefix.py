import discord
from datetime import datetime
import serverdatastore

async def command(bot, guild, message, command, args):
    if ("administrator", "False") in message.author.guild_permissions:
        return
    datastore = serverdatastore.jsonDatastore
    prefix = datastore["servers"][f"{guild.id}"]["prefix"]
    if len(args) == 0:
        embed = discord.Embed(title="Error.", description=f"Usage: {prefix}setprefix <newprefix>", colour=discord.Colour.red())
        embed.set_footer(text="Made by the Microbox Team")
        embed.timestamp = datetime.utcnow()
        await message.channel.send(embed=embed)
        return
    newPrefix = " ".join(args)
    datastore["servers"][f"{guild.id}"]["prefix"] = newPrefix 
    serverdatastore.writeServersJson(datastore)
    embed = discord.Embed(title="Success!", description=f"Successfully changed the server prefix from '{prefix}' to '{newPrefix}'.", colour=discord.Colour.green())
    embed.set_footer(text="Made by the Microbox Team")
    embed.timestamp = datetime.utcnow()
    await message.channel.send(embed=embed)

    