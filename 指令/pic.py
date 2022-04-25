import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import random
import json

with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

class Pic(Cog_ext):

    @commands.command()#傳送檔案中的隨機一張圖片
    async def 圖片(self, ctx):
        ran_pic = random.choice(jdata['pic1'])
        pic = discord.File(ran_pic)
        await ctx.send(file = pic)

    @commands.command()#傳送n站網址
    async def n(self, ctx, number):
        self.number = number
        await ctx.send(f'https://nhentai.net/g/{number}/')

    @commands.command()#傳送p站網址
    async def p(self, ctx, number):
        self.number = number
        await ctx.send(f'https://www.pixiv.net/artworks/{number}')

def setup(bot):
    bot.add_cog(Pic(bot))