import discord
from discord.ext import commands
from 核心.classes import Cog_ext

class Main(Cog_ext):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping: {round(self.bot.latency*1000)}(毫秒)')

def setup(bot):
    bot.add_cog(Main(bot))