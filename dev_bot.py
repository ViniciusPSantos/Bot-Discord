import discord 

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    message.channel.send('Hi')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("NzQ4MzMzNjY1MzcyNzMzNTMw.X0b6CQ.EJFHgcVrXn3yRD4nKH8wfAO53U0")

#a