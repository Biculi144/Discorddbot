import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='X-MEN l ROLEPLAY'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '?ipsever':
        await client.send_message(message.channel,'Day la ip sv : 116.96.19.204')
    if message.content == '?img':
        em = discord.Embed(description='vui nhi?')
        em.set_image(url='https://ichef.bbci.co.uk/images/ic/704xn/p05hr20h.jpg')
        await client.send_message(message.channel, embed=em)
    if ('Xin chao') in message.content:
       await client.delete_message(message)
client.run('NjA5NTUxMDk1MTQ4MDUyNDk5.XU4Www.CeH7p-1e_DnzpwtfYmu-1eiyX1c')
