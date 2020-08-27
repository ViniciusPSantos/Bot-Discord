import discord
from discord.ext.commands import AutoShardedBot, when_mentioned_or

#Lista de modulos
modulos = []

#Evento do client
client = AutoShardedBot(command_prefix="!", case_insensitive=True)

#evento do on_ready
@client.event
async def on_ready():
    print(f"{client.user.name}Online")
    await client.change_presence(activity=discord.Game(name="Programando"),status="Online")

#carregar modulos 
if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)

    client.run("NzQ4MzMzNjY1MzcyNzMzNTMw.X0b6CQ.Z7tVL3fxYyr_asfARZvbktqRHt0")