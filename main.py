import discord
import os
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    jsonStr = json.dumps(client)
    print(jsonStr)

    if message.content.startswith('`hello'):
        await message.channel.send('Hello!')

client.run("ODM0NzE5MzQ2MTA1Mzg0OTgx.YIE--A.bJlE_Lzu_CY2VKE0Hgm_fQrAHfk")