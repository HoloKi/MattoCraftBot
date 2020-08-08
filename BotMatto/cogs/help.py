import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help is online.")

    # COMANDO PER LE FAQ

    @commands.command()
    async def faq(self, ctx):
        embed = discord.Embed(color= discord.Color.red())
        embed.add_field(name="FAQ", value = 'Per vedere il FAQ entra in questo link: https://telegra.ph/FAQ-08-07-4',inline=False)
        idutente = ctx.message.author.id
        user = self.client.get_user(idutente)
        await user.send(embed=embed)
        #await ctx.send(embed=embed)

    #COMANDO PER VOTARE
    @commands.command()
    async def voto(self, ctx):
        embed = discord.Embed(color= discord.Color.red())
        embed.add_field(name="Per votare", value = 'Ho sentito che hai chiesto del voto, guardati questo video: https://www.youtube.com/watch?v=erL30ZKf7bI',inline=False)
        await ctx.send(embed=embed)

    #COMANDO STAFF
    @commands.command()
    async def staff(self, ctx):
        embed = discord.Embed(color= discord.Color.red())
        embed.set_author(name='Lo staff di MattoCraft')
        embed.add_field(name = 'Owner', value = 'Gianma23', inline=False)
        embed.add_field(name = 'Mod', value = 'JwZy', inline=False)
        embed.add_field(name = 'Helper', value = 'ArmerGaggy, YumiFox', inline=False)
        await ctx.send(embed=embed)

    #COMANDO YOUTUBE
    @commands.command()
    async def youtube(self,ctx):
        embed = discord.Embed(color = discord.Color.blue())
        embed.set_author(name='Canale ufficiale')
        await ctx.send(embed=embed)
        await ctx.send('https://www.youtube.com/channel/UCXUgfilc-mLPEVW3HkfRvjg')


    #COMANDO HELP
    @commands.command(pass_context = True)    
    async def help(self, ctx):
        embed = discord.Embed(
            color = discord.Colour.orange()  
        )
        
        embed.set_author(name='Help')
        embed.add_field(name = '.faq', value = 'Ti indirizza alle faq del server', inline=False)
        embed.add_field(name = '.voto', value = 'Se vuoi visualizzare la guida per votare!', inline=False)
        embed.add_field(name = '.staff', value = 'Per conoscere lo staff di Mattocraft!', inline=False)
        embed.add_field(name = '.segnalazione', value = 'usa il comando segnalazione + frase per segnalare qualcosa', inline=False)
        embed.add_field(name='.youtube', value= 'Visualizza il canale ufficiale del server', inline=False)
        
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Help(client))
