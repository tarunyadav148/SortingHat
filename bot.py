import discord
from discord.ext import commands


from hogwarts import SortingHat
from database import Database

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
        desc = SortingHat.getBoldHouseTitile(my_house)
        color = SortingHat.getColor(my_house)
        embed = discord.Embed(title=title,description=desc,color=color)
        url = SortingHat.getHouseIcon(my_house)
        embed.set_image(url=url)
        await ctx.reply(embed=embed)


    #getting reuired fields
    my_house = SortingHat.getHouse()
    title = f'__Where to put you {ctx.author.display_name} ?__ \nHmmmm...'
    color = SortingHat.getColor(my_house)
    desc = SortingHat.getBoldHouseTitile(my_house)

    #adding to database
    db = Database()
    db.addMemeber(str(ctx.author.id),my_house)
    db.close()

    #making an embed
    embed = discord.Embed(title=title,description=desc,color=color)
    url = SortingHat.getHouseIcon(my_house)
    embed.set_image(url=url)


    await ctx.reply(embed=embed)

@bot.command()
async def pleasechange(ctx):
    
    db = Database()
    id = str(ctx.author.id)
    if(db.isMemberHadHouse(id) == False):
        await ctx.reply('{} is not a member of any house'.format(ctx.author.display_name))
        return

     #getting reuired fields
    my_house = SortingHat.getHouse()
    title = f'__If you insist {ctx.author.display_name} ?__ \nBut where to put you?'
    color = SortingHat.getColor(my_house)
    desc = SortingHat.getBoldHouseTitile(my_house)

    #adding to database
    db = Database()
    db.updateMeberHouse(str(ctx.author.id),my_house)
    db.close()

    #making an embed
    embed = discord.Embed(title=title,description=desc,color=color)
    url = SortingHat.getHouseIcon(my_house)
    embed.set_image(url=url)


    await ctx.reply(embed=embed)


@bot.command()
async def myhouse(ctx):

    db = Database()
    if(db.isMemberHadHouse(str(ctx.author.id))):
        my_house = db.getHouseOfMember(str(ctx.author.id))
        title = 'Member of House'
        desc = SortingHat.getBoldHouseTitile(my_house)
        color = SortingHat.getColor(my_house)
        embed = discord.Embed(title=title,description=desc,color=color)
        url = SortingHat.getHouseIcon(my_house)
        embed.set_image(url=url)
        await ctx.reply(embed=embed)
    else:
        return await ctx.reply('{} is not a member of any house'.format(ctx.author.display_name))


bot.run(os.getenv('TOKEN'))