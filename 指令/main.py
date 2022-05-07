import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import random
import json

with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

class Main(Cog_ext):

    @commands.command()#偵測延遲
    async def ping(self, ctx):
        await ctx.send(f'Ping: {round(self.bot.latency*1000)}(毫秒)')

    @commands.command()#查到的py教學
    async def 大大(self, ctx):
        await ctx.send('Proladon大大:https://www.youtube.com/playlist?list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN')

    @commands.command()#刪除並複誦我說的話
    async def botsay(self, ctx, *, msg):#'*'後都會被當作msg參數
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit = num +1)

    @commands.command()
    async def talk(self, ctx):
        ran_talk = random.choice(jdata['talk'])
        await ctx.send(ran_talk)

def setup(bot):
    bot.add_cog(Main(bot))
