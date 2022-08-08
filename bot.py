import discord
from discord.ext import commands
import json
import os
import keep_alive


with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='^', intents = intents, help_command = None, owner_id = int(jdata['OWNER']))


@bot.event
async def on_ready():
    print("testing")

@bot.command()#上傳指令分類
async def load(ctx, ext):
    bot.load_extension(f'指令.{ext}')
    await ctx.send(f'Loaded {ext} done.')

@bot.command()#刪除指令分類
async def unload(ctx, ext):
    bot.unload_extension(f'指令.{ext}')
    await ctx.send(f'Unloaded {ext} done.')

@bot.command()#重啟指令分類
async def reload(ctx, ext):
    bot.reload_extension(f'指令.{ext}')
    await ctx.send(f'Reloaded {ext} done.')



for Filename in os.listdir('./指令'):
    if Filename.endswith('.py'):
        bot.load_extension(f'指令.{Filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(os.environ['token'])
