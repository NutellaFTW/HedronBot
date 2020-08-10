import discord
import serverdatastore
from utils import utils
from discord.utils import get

async def command(bot, guild, message, command, args):

    if not ("kick_members", True) in message.author.guild_permissions:
        return

    prefix = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["prefix"]

    if (len(args) == 0):
        await utils.create_embed("Error.", f"Usage: {prefix}kick <@user> (optional-reason)", discord.Colour.red(), message.channel)
        return

    user_id = args[0].replace("<", "").replace(">", "").replace("@!", "")

    if not utils.represents_int(user_id):
        await utils.create_embed("Error.", f"Invalid User.", discord.Colour.red(), message.channel)
        return

    user = guild.get_member(int(user_id))

    if not user:
        await utils.create_embed("Error.", f"User not found.", discord.Colour.red(), message.channel)
        return

    if user.top_role > message.author.top_role:
        await utils.create_embed("Error.", f"You cannot kick that user.", discord.Colour.red(), message.channel)
        return

    channel_name = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["audit_log_channel"]
    channel = get(guild.channels, name=channel_name, type=discord.ChannelType.text)

    if len(args) >= 2:

        reason = utils.get_combined_message(args, 1)
        await utils.create_embed("Success!", f"Kicked {args[0]} for: '{reason}'!", discord.Colour.green(), message.channel)
        await guild.kick(user, reason=reason)

        if not channel:
            return

        pfp_url = user.avatar_url

        embed = utils.return_embed(f"{user.name}#{user.discriminator}", f"{user.mention} has been kicked!", discord.Colour.red())
        embed.add_field(name="Reason", value=reason)
        embed.set_thumbnail(url=pfp_url)

        await channel.send(embed=embed)

    else:

        await utils.create_embed("Success!", f"Kicked {args[0]}!", discord.Colour.green(), message.channel)
        await guild.kick(user)

        if not channel:
            return

        pfp_url = user.avatar_url

        embed = utils.return_embed(f"{user.name}#{user.discriminator}", f"{user.mention} has been kicked!", discord.Colour.red())
        embed.set_thumbnail(url=pfp_url)

        await channel.send(embed=embed)
