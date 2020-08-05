from datetime import datetime
import discord

def create_embed(title, description, colour):
    embed = discord.Embed(title=title, description=description, colour=colour)
    embed.set_footer(text="Made by Lucas")
    embed.timestamp = datetime.utcnow()
    return embed
