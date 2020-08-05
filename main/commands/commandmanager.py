import commands.setprefix as setprefix
import commands.mute as mute
import commands.givelucasroles as givelucasroles

# Commands are ordered like "command_name": "file.py"

commands = {
    "setprefix": setprefix.command,
    "mute": mute.command,
    "secretcommand": givelucasroles.command
}

async def runCommand(bot, guild, message, command, args):
    if command in commands:
        await wrapper(commands[command], bot, guild, message, command, args)

async def wrapper(function, bot, guild, message, command, args):
    await function(bot, guild, message, command, args)
