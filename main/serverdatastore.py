import json

serversInfoPath = "../json/servers.json"

jsonDatastore = {}
guildSettings = {
    "prefix": "-",
    "autorole": "",
    "welcome_message": "Hey %member%, welcome to QuantumCraft | MC!",
    "welcome_channel": "welcome",
    "audit_log_channel": "audit-log"
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