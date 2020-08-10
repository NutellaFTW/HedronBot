from utils import utils
import discord
import serverdatastore

async def command(bot, guild, message, command, args):

    if not ("manage_messages", True) in message.author.guild_permissions:
        return

    channel = message.channel

    prefix = serverdatastore.jsonDatastore["servers"][f"{guild.id}"]["prefix"]

    if (len(args) == 0):
        await utils.create_embed("Error.", f"Usage: {prefix}purge <amount> (optional-@user)", discord.Colour.red(), message.channel)
        return

    if not utils.represents_int(args[0]):
        await utils.create_embed("Error.", "Invalid amount.", discord.Colour.red(), message.channel)
        return

    limit = int(args[0])

    if (len(args) == 2):

        user_id = args[1].replace("<", "").replace(">", "").replace("@!", "")

        if not utils.represents_int(user_id):
            await utils.create_embed("Error.", f"Invalid User.", discord.Colour.red(), message.channel)
            return

        user = guild.get_member(int(user_id))

        if not user:
            await utils.create_embed("Error.", f"User not found.", discord.Colour.red(), message.channel)
            return

        def is_user(message):
            return message.author == user

        await channel.purge(limit=limit, check=is_user)

        await utils.create_embed("Success!", f"Attempting to purge last {limit} messages if sender is {user.mention}!", discord.Colour.green(), message.channel)

    else:
        await channel.purge(limit=limit)
        await utils.create_embed("Success!", f"Attempting to purge last {limit} messages!", discord.Colour.green(), message.channel)
    
