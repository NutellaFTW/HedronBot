import commands.setprefix as setprefix
import commands.canada as canada
import commands.funny as funny

# Commands are ordered like "command_name": "file.py"

commands = {
    "setprefix": setprefix.command,
    "canada": canada.command,
    "funny": funny.command
}

async def runCommand(bot, guild, message, command, args):
    if command in commands:
        await wrapper(commands[command], bot, guild, message, command, args)

async def wrapper(function, bot, guild, message, command, args):
    await function(bot, guild, message, command, args)
