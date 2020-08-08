import discord
import os
from discord.ext import commands
import time
import logging


client = commands.Bot(command_prefix = '.')
client.remove_command('help')

game = discord.Streaming(name='MattoCraft',url='https://www.youtube.com/watch?v=f6AWapxwb2s&feature=youtu.be',game='MattoCraft')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Il bot è pronto e funzionante.')
    print(client.user.name)
    print(client.user.id)
    print('------')



#check if there is a .py inside the cogs directory and load it
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



client.run('')



