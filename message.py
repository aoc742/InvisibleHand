import asyncio

class Message():
    def __init__(self, client):
        self.client = client

    async def handle(self, message):
        # msg = await self.client.send_message(message.channel, '{0} said:\n{1}'.format(message.author.name, message.content), tts=True)
        # await self.client.delete_message(msg)
        # return

        if not message.content.startswith('!'):
            return

        if message.content.startswith('!deleteme'):
            msg = await self.client.send_message(message.channel, 'I will delete myself now...')
            await self.client.delete_message(msg)
        
        if message.content.lower().startswith('!help'):
            #display help message
            msg = 'List of commands:\n'
            msg += 'To create a new TTS command, type "!create tts [command name] [text]\n'
            msg += 'example: !create tts magnets "Magnets rule!\n'
            msg += 'or: !create tts !magnets Magnets rule!\n'
            msg += 'Type !magnets in chat to test out your new TTS command!\n'

        #if message.content.lower().startswith('!create'):
            