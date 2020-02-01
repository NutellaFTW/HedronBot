import json

serversInfoPath = "json/servers.json"

jsonDatastore = {}
guildSettings = {
    "prefix": "-"
    }

def updateDatastore( ):
    with open(serversInfoPath, "r") as jsonFile:
        global jsonDatastore
        jsonDatastore = json.load(jsonFile)

def writeServersJson(data):
    with open(serversInfoPath, "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)
    updateDatastore()

def addServer(guild):
    data = jsonDatastore
    data["servers"][guild.id] = guildSettings
    writeServersJson(data)

def removeServer(guild):
    data = jsonDatastore
    del data["servers"][f"{guild.id}"]
    writeServersJson(data)

def getServerExists(guild):
    data = jsonDatastore
    if f"{guild.id}" in data["servers"]:
        return True
    return False