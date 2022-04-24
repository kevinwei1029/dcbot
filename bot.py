import discord
from discord.ext import commands
import json

with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/',intents = intents)

@bot.event
async def on_ready():
    print("testing")

#@bot.event
#async def on_guild_emojis_update():
#    channel = bot.get_channel(int(jdata['Test_gen_channel']))
#    await channel.send("有新表情喔!")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(bot.latency*1000)}(毫秒)')

@bot.command()
async def 圖片(ctx):
    pic = discord.File(jdata['pic1'])
    await ctx.send(file = pic)


bot.run(jdata['TOKEN'])