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
async def on_message(message):
    if message.author == client.user:
        return
    user = rf(message.author)
    messages = await message.channel.history(limit=30).flatten()
    if messages[29].created_at.second + 20 <= messages[0].created_at.second:
        await message.channel.send(f'Arrête de spam {user} !')
    for elem in element:
        if elem in message.content.lower():
            await message.channel.send(f'Bonjour à toi {user} !')
            break
    await client.process_commands(message)


def connect_server():
    try:
        client.run(TOKEN)
    except RuntimeError as error:
        print(error, "Server close")
        return
