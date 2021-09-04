import discord
from hogwarts import SortingHat

def get_embed(house,title):
    desc = get_bold(house)
    color = SortingHat.getColor(house)
    embed = discord.Embed(title=title,description=desc,color=color)
    url = SortingHat.getHouseIcon(house)
    embed.set_image(url=url)
    return embed

def get_bold(house):
    return "**"+house+"**"