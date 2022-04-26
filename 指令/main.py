import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import datetime

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
    
    @commands.has_permissions(administrator=True)#需要有管理員權限
    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit = num +1)

    # @commands.command()
    # async def emd(self, ctx):
    #     embed=discord.Embed(title="水滴能幹嘛", url="https://reurl.cc/NAXqLp", color=0x55dbdd, timestamp=datetime.datetime.now())
    #     embed.set_author(name="水滴。")
    #     embed.set_thumbnail(url="https://i.imgur.com/O6UbyuNh.jpg")
    #     embed.add_field(name="水滴聊天 -", value="水滴能回覆的所有訊息", inline=False)
    #     embed.add_field(name="水滴指令 -", value="水滴能使用的指令", inline=False)
    #     embed.set_footer(text="看三小")
    #     await ctx.send(embed=embed)

    # @commands.command()
    # async def clean(self, ctx, num: int):
    #    if ctx.message.author.guild_permissions.administrator:
    #        await ctx.channel.purge(limit = num +1)
    #    else:
    #        await ctx.send('你沒有權限使用此指令')

def setup(bot):
    bot.add_cog(Main(bot))