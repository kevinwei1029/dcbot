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
    async def n(self, ctx, number):
        await ctx.send(f'https://nhentai.net/g/{number}/')

    @commands.command()#傳送禁漫網址
    async def j(self, ctx, number):
        await ctx.send(f'https://18comic.org/photo/{number}')

    @commands.command()#傳送p站網址
    async def p(self, ctx, number):
        await ctx.send(f'https://www.pixiv.net/artworks/{number}')

    @commands.command()#大喜利
    async def giri(self, ctx, *, msg):
        giri = [f"GOOGLE做的煮飯器會有什麼功能存在?{msg}。",
                f"A：「愛是什麼？」\nB(你)：「{msg}。」",
                f"你的戀人從20年的植物人狀態中甦醒過來了，你會對他（她）說什麼？{msg}。",
                f"什麼看起來很普通的事，在凌晨三點時做，看起來就很可疑？{msg}。",
                f"台灣最大的玩笑是{msg}。",
                f"今天，我要表演把{msg}塞進嘴裡。"]
        rangiri = random.choice(giri)
        await ctx.send(rangiri)

def setup(bot):
    bot.add_cog(Pic(bot))
