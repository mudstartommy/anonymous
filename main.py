import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Online")
    await client.change_presence(game=discord.Game(name="'Hidden'"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")
client.run(TOKEN)
