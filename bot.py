import discord
from discord import embeds
from discord.ext import commands

from hogwarts import SortingHat
from database import Database
from helper import get_embed

import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))



@bot.command()
async def onmyhead(ctx):
    #check allready had house
    db = Database()
    if(db.isMemberHadHouse(str(ctx.author.id))):
        my_house = db.getHouseOfMember(str(ctx.author.id))
        title = 'Already member of House'
        embed = get_embed(house=my_house,title=title)
        await ctx.send(embed=embed)
        return

    #getting reuired fields
    my_house = SortingHat.getHouse()
    title="I know just what to do with you..."

    await ctx.send(f"Ah! {ctx.author.display_name}")

    #adding to database
    db = Database()
    db.addMemeber(str(ctx.author.id),my_house)
    db.close()

    #getting an embed
    embed = get_embed(house=my_house,title=title)

    await ctx.send(embed=embed)




@bot.command()
async def pleasechange(ctx):  
    db = Database()
    if(db.isMemberHadHouse(id = str(ctx.author.id)) == False):
        await ctx.send('{} is not a member of any house'.format(ctx.author.display_name))
        return

    #getting reuired fields
    my_house = SortingHat.getHouse()
    title = "Well if you're sure, better be... "

    #adding to database
    db = Database()
    old_house = db.getHouseOfMember(id=str(ctx.author.id))
    db.updateMeberHouse(str(ctx.author.id),my_house)
    db.close()

    await ctx.send("It's all here in your head.")
    await ctx.send("And {} will help you on the way to greatness,".format(old_house))
    await ctx.send("there's no doubt about that. No?")
    await ctx.send(f'*If you insist {ctx.author.display_name}*')
    await ctx.send('But where to put you?')

    #getting an embed
    embed = get_embed(house=my_house,title=title)

    await ctx.send(embed=embed)




@bot.command()
async def myhouse(ctx):
    db = Database()
    if(db.isMemberHadHouse(id=str(ctx.author.id))):
        my_house = db.getHouseOfMember(str(ctx.author.id))
        title = 'Member of House'
        embed = get_embed(house=my_house,title=title)
        await ctx.send(embed=embed)
    else:
        await ctx.send('{} is not a member of any house'.format(ctx.author.display_name))




@bot.command()
async def loc(ctx):
    embed=discord.Embed(title="List of commands", description="", color=discord.Color.dark_gray())
    embed.add_field(name="$onmyhead", value="To get a house", inline=False)
    embed.add_field(name="$myhouse", value="To display your house", inline=False)
    embed.add_field(name="$pleasechange", value="To change your house", inline=False)
    await ctx.send(embed=embed)


bot.run(os.getenv('TOKEN'))