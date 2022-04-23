import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print("testing")

bot.run('OTY2NzI5NTQyOTU1ODM5NTQ5.YmF_DA.Wp4-l3BJIO8XesXb7TJT8SiU_3E')