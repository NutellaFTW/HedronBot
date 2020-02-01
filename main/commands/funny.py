import random
import csv

jokes = []

with open("jokes.txt", "r") as file:
        csvReader = csv.reader(file, delimiter="\n")
        for joke in csvReader:
            if len(joke) != 0:
                jokes.append(joke[0].replace(",", ""))

async def command(bot, guild, message, command, args):
    await message.channel.send(random.choice(jokes))
