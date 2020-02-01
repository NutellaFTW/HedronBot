import discord
import json
import aiohttp
import serverdatastore
from commands import commandmanager
from utils import aiosession

botInfoPath = "json/botinfo.json"

class Bot:

    def __init__(self):
        self.client = discord.Client()
        self.token = self.setToken()
        self.clientId = self.jsonDatastore["client_id"]

    def setToken(self):
        with open(botInfoPath, "r") as jsonFile:
            self.jsonDatastore = json.load(jsonFile)
            return self.jsonDatastore["token"]

    def run(self):
        self.client.run(self.token)

# Initializing Bot Class
bot = Bot()
serverdatastore.updateDatastore()

client = bot.client

#aiosession.runSession(client)

# this sells microbot's egg; you can drink the yolk 

@client.event
async def on_ready():

    oauth_url = discord.utils.oauth_url(bot.clientId, permissions=discord.Permissions(permissions=8))
    print("Bot is Ready")
    print(f"Invite link: {oauth_url}")

    for guild in client.guilds:
        serverExists = serverdatastore.getServerExists(guild)
        print(f"Checking {guild.name}: {serverExists}")
        if not serverExists:
            serverdatastore.addServer(guild)

@client.event
async def on_guild_join(guild):
    serverdatastore.addServer(guild)

@client.event
async def on_guild_remove(guild):
    serverdatastore.removeServer(guild)

@client.event
async def on_message(message):
    # Rerouting messages to commands if they start with server's prefix
    guildId = message.guild.id
    if f"{guildId}" not in serverdatastore.jsonDatastore["servers"]:
        return
    prefix = serverdatastore.jsonDatastore["servers"][f"{guildId}"]["prefix"]
    if message.content.startswith(prefix):
        splitMessage = message.content.split(" ")
        strippedMessage = splitMessage[1:]
        strippedMessage.insert(0, splitMessage[0][len(prefix):])
        command = strippedMessage[0]
        args = strippedMessage[1:]
        await commandmanager.runCommand(client, message.guild, message, command, args)


bot.run() 


