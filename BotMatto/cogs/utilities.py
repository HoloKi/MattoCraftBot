import discord
from discord.ext import commands
import random
import asyncio
import random
import datetime

class Util(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Util is online.")

    
    #COMANDO PER SCRIVERE NEL CANALE OFFERTE PER NERDS

    @commands.command()
    @commands.has_role("Tester")
    async def segnalazione(self, ctx,*, arg):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(color = discord.Colour.green())
        nome= ctx.message.author
        avatar = ctx.message.author.avatar_url
        embed.set_author(name=nome,icon_url=avatar)
        embed.add_field(name='Segnalazione:',value =arg)
        embed.timestamp = datetime.datetime.utcnow()
        channel = self.client.get_channel(741654564612341840)
        await channel.send(embed=embed)

    @segnalazione.error
    async def segnalazione_error(self,ctx, error):
        if isinstance(error, commands.errors.MissingRole):
            await ctx.send('Non hai i permessi!')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Manca l'argomento, scrivi .segnalazione <messaggio> ")


    #COMANDO PER AVERE L'AVATAR DELL'UTENTE PINGATO
    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(color = discord.Colour.blue())
        nome= ctx.message.author
        userAvatarUrl = avamember.avatar_url
        avatar = ctx.message.author.avatar_url
        embed.set_author(name=nome,icon_url=avatar)
        embed.set_image(url=userAvatarUrl)
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Util(client))