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


## information from env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER_NAME = os.getenv("DISCORD_GUILD")


## connection to discord
client = dc.Client()


@client.event
async def on_ready():
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
    for elem in element:
        if elem in message.content.lower():
            await message.channel.send(f'Bonjour à toi {user} !')
            break


def connect_server():
    client.run(TOKEN)
