import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import json, asyncio, datetime

with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

class Task(Cog_ext):
    def __init__(self, *args, **kwargs):#task初始化
        super().__init__(*args, **kwargs)#賦予classes的初始資料
        
        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(int(jdata['Test_gen_channel']))
        #     while not self.bot.is_closed():
        #         await self.channel.send('Ok,testing!')
        #         await asyncio.sleep(10)#延遲為10秒

        # self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(int(jdata['Test_gen_channel']))
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%m%d')
                pass

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel: {self.channel.mention}')#mention: tag頻道/人

    @commands.command()
    async def set_time(self, ctx, time):
        with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json', mode='w', encoding='utf8') as jfile: #'w'=write(寫入)
            json.dump(jdata, jfile, indent = 4)#indent =縮排


def setup(bot):
    bot.add_cog(Task(bot))