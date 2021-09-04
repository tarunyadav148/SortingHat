import random
import discord

class SortingHat():

    def getHouse():
        HOUSE = ['Godric Gryffindor','Rowena Ravenclaw','Helga Hufflepuff','Salazar Slytherin']
        house = random.choice(HOUSE)
        return house

    def getColor(house):
        HOUSE_COLOR = {
            'Godric Gryffindor':discord.Color.dark_red(),
            'Rowena Ravenclaw':discord.Color.dark_blue(),
            'Helga Hufflepuff':discord.Color.from_rgb(255, 255, 0),
            'Salazar Slytherin':discord.Color.dark_green()
            }
        return HOUSE_COLOR[house]
    
    def getHouseIcon(house):
        HOUSE_ICON = {
            'Godric Gryffindor':'https://i.pinimg.com/originals/ea/e2/d2/eae2d2d92754dc560f67dc802b518f2b.jpg',
            'Rowena Ravenclaw':'https://e7.pngegg.com/pngimages/563/589/png-clipart-ravenclaw-logo-ravenclaw-house-fictional-universe-of-harry-potter-common-room-hogwarts-gryffindor-harry-potter-ravenclaw-logo-helga-hufflepuff-thumbnail.png',
            'Helga Hufflepuff':'https://www.kindpng.com/picc/m/19-199438_clipart-house-harry-potter-hufflepuff-transparent-background-hd.png',
            'Salazar Slytherin':'https://c0.klipartz.com/pngpicture/594/270/gratis-png-slytherin-house-accesorios-para-telefonos-moviles-hogwarts-gryffindor-lord-voldemort-slytherin.png'
            }
        return HOUSE_ICON[house]

    # def getBoldHouseTitile(house):
    #     return "**"+house+"**"
    
    # def getEmbed(house,title):
    #     desc = SortingHat.getBoldHouseTitile(house)
    #     color = SortingHat.getColor(house)
    #     embed = discord.Embed(title=title,description=desc,color=color)
    #     url = SortingHat.getHouseIcon(house)
    #     embed.set_image(url=url)
    #     return embed