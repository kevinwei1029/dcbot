from ast import For, If
import discord
from discord.ext import commands
import json
import random
import os

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




for Filename in os.listdir('./指令'):#./為相對路徑，也可直接給完整路徑
    if Filename.endswith('.py'):
        bot.load_extension(F'指令.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])