import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/',intents = intents)

@bot.event
async def on_ready():
    print("testing")

#@bot.event
#async def on_guild_emojis_update():
#    channel = bot.get_channel(966727218048925699)
#    await channel.send("有新表情喔!")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(bot.latency*1000)}(毫秒)')

bot.run('OTY2NzI5NTQyOTU1ODM5NTQ5.YmF_DA.Wp4-l3BJIO8XesXb7TJT8SiU_3E')