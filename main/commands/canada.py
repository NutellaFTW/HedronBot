import discord
import random
from bs4 import BeautifulSoup
import urllib, aiohttp, io

url = "https://imgur.com/search/score?q=canada+meme"

async def command(bot, guild, message, command, args):

    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, features="html.parser")
    links = []

    for link in soup.findAll("a", href=True):
        href = link.get("href")
        if "gallery" in href:
            links.append(f"https://imgur.com{href}")

    randomLink = random.choice(links)

    await message.channel.send(randomLink)
