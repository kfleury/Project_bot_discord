##
## Personal Project made by:
## killian.fleury@epitech.eu
##
## Project Description:
## function server
##
import os
import discord as dc
from function import reformat_user as rf
from function import is_spam
from function import message as element
from dotenv import load_dotenv
from discord.ext import commands


## global variables
counter_global = 5


## information from env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER_NAME = os.getenv("DISCORD_GUILD")


## connection to discord
client = commands.Bot(command_prefix='!')


@client.command()
async def foo(ctx, arg: str):
    await ctx.send(arg)


@client.event
async def on_ready():
    ## init status
    game = dc.Game("Je mange des chats")
    await client.change_presence(status=dc.Status.idle, activity=game)
    ## display guild name
    guild = dc.utils.get(client.guilds, name=SERVER_NAME)
    print(f'{client.user} has connected to the following server:')
    print(f'{guild} on Discord !\n')
    ## display member name
    members = client.get_all_members()
    print('Guild Members:')
    for ppl in members:
        print(f' - {ppl}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Bonjour {member.name}, Bienvenue sur mon serveur Discord !'
    )


@client.event
async def on_typing(channel, user, when):
    async for message in channel.history(limit=200):
        if message.author != client.user:
            is_spam(message, user, when)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for elem in element:
        if elem in message.content.lower():
            user = rf(message.author)
            await message.channel.send(f'Bonjour à toi {user} !')
            break
    await client.process_commands(message)


def connect_server():
    try:
        client.run(TOKEN)
    except RuntimeError as error:
        print(error, "Server close")
        return
