from ast import For, If
import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='^', intents = intents, help_command = None, owner_id = int(jdata['OWNER']))

@bot.event
async def on_ready():
    print("testing")

@commands.is_owner()#限擁有者使用
@bot.command()#上傳指令分類
async def load(ctx, ext):
    bot.load_extension(f'指令.{ext}')
    await ctx.send(f'Loaded {ext} done.')

@commands.is_owner()
@bot.command()#刪除指令分類
async def unload(ctx, ext):
    bot.unload_extension(f'指令.{ext}')
    await ctx.send(f'Unloaded {ext} done.')

@commands.is_owner()
@bot.command()#重啟指令分類
async def reload(ctx, ext):
    bot.reload_extension(f'指令.{ext}')
    await ctx.send(f'Reloaded {ext} done.')

#@bot.command()#上傳指令分類
#async def load(ctx, ext):
#    if ctx.message.author.id == int(jdata['OWNER']):
#        bot.load_extension(f'指令.{ext}')
#        await ctx.send(f'Loaded {ext} done.')
#    else:
#        await ctx.send('你沒有權限使用此指令')




for Filename in os.listdir('./指令'):#./為相對路徑，也可直接給完整路徑
    if Filename.endswith('.py'):
        bot.load_extension(f'指令.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])