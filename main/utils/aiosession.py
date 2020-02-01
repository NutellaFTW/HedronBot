import aiohttp

session = ""

def runSession(client):
    global session
    global browser
    session = aiohttp.ClientSession(loop=client.loop)