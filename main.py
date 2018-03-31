#!/usr/bin/python3

import discord
import asyncio
import time
from message import Message
from configuration import Configuration

config = Configuration().get()
client = discord.Client()
messageHandler = Message(client)

@client.event
async def on_ready():
    if config['assert']:
        print('Logged in as ' + client.user.name + ' - ' + client.user.id)
        print('\nVoice clients:\n' + '\n'.join(str(vcs) for vcs in client.voice_clients))
        print('\nServers:\n' + '\n'.join(str(server) for server in client.servers))
        print('\nAll Channels:\n' + '\n'.join(str(p) for p in client.get_all_channels()))
        print('\nAll members:\n' + '\n'.join(str(member) for member in client.get_all_members()))
    print('Ready')

@client.event
async def on_message(message):
    # stop bot from replying to itself
    if message.author == client.user:
        return
    await messageHandler.handle(message)

@client.event
async def on_message_edit(before, after):
    # stop bot from replying to itself
    if before.author == client.user:
        return

    fmt = '**{0.author}** edited their message from {0.timestamp}. Original Message:\n{1.content}'
    await client.send_message(after.channel, fmt.format(after, before))

@client.event
async def on_message_delete(message):
    # stop bot from replying to itself
    if message.author == client.user:
        return

    fmt = 'Message by {0.author.name} from {0.timestamp} has been deleted. Original message:\n{0.content}'
    await client.send_message(message.channel, fmt.format(message))

@client.event
async def on_voice_state_update(before, after):
    if before.voice.voice_channel == None and after.voice.voice_channel != None:
        for channel in after.server.channels:
            if channel.type is not str and channel.type != 4 and channel.type.value == 0:
                if str(after) == 'Gameandwatch#3862':
                    time.sleep(1)
                    msg = await client.send_message(channel, "Wassup y'all It's me It's your boy Asmin gold", tts = True)
                    await client.delete_message(msg)
                return

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='channel_id_here')
    while not client.is_closed:
        counter += 1
        await client.send_message(channel, counter)
        await asyncio.sleep(60) # task runs every 60 seconds

#client.loop.create_task(my_background_task)
client.run(config['token'])
