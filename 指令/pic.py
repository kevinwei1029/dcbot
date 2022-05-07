import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import random
import json

with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

class Pic(Cog_ext):

    @commands.command()#傳送檔案中的隨機一張圖片
    async def pic(self, ctx):
        ran_pic = random.choice(jdata['pic1'])
        await ctx.send(f'https://cdn.discordapp.com/attachments/966727218048925699/{ran_pic}')

    @commands.command()#傳送n站網址
    async def n(self, ctx, fun, *, tag):
        tag = tag.replace(" ", "-")
        if fun == 'n':
            await ctx.send(f'https://nhentai.net/g/{tag}/')
        elif fun == 'a':
            await ctx.send(f'https://nhentai.net/artist/{tag}/')
        elif fun == 'c':
            await ctx.send(f'https://nhentai.net/character/{tag}/')
        elif fun == 't':
            await ctx.send(f'https://nhentai.net/tag/{tag}/')
        elif fun == 'p':
            await ctx.send(f'https://nhentai.net/parody/{tag}/')



    @commands.command()#傳送p站網址
    async def p(self, ctx, number):
        await ctx.send(f'https://www.pixiv.net/artworks/{number}')

def setup(bot):
    bot.add_cog(Pic(bot))
