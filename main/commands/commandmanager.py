import commands.setprefix as setprefix
import commands.mute as mute
import commands.givelucasroles as givelucasroles
import commands.ban as ban
import commands.kick as kick
import commands.autorole as autorole
import commands.setwelcomemessage as setwelcomemessage
import commands.purge as purge
import commands.setauditlog as setauditlog
import commands.setwelcomechannel as setwelcomechannel

# Commands are ordered like "command_name": "file.py"

commands = {
    "setprefix": setprefix.command,
    "mute": mute.command,
    "secretcommand": givelucasroles.command,
    "ban": ban.command,
    "kick": kick.command,
    "setautorole": autorole.command,
    "setwelcomemessage": setwelcomemessage.command,
    "purge": purge.command,
    "setauditlog": setauditlog.command,
    "setwelcomechannel": setwelcomechannel.command
}

async def runCommand(bot, guild, message, command, args):
    if command in commands:
        await wrapper(commands[command], bot, guild, message, command, args)

async def wrapper(function, bot, guild, message, command, args):
    await function(bot, guild, message, command, args)
