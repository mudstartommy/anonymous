import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Online")
    await client.change_presence(game=discord.Game(name="'Hidden'"))
