import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import json, asyncio, datetime

with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

class Task(Cog_ext):
    def __init__(self, *args, **kwargs):#task初始化
        super().__init__(*args, **kwargs)#賦予classes的初始資料
        
        self.counter = 0
    

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(966727218048925699)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.counter == 0:
                    self.counter = 1
                    await self.channel.send("It's time to play phigros!!")
                    await asyncio.sleep(1)
                else:    
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel: {self.channel.mention}')#mention: tag頻道/人

    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0
        with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json', mode='w', encoding='utf8') as jfile: #'w'=write(寫入)
            json.dump(jdata, jfile, indent = 4)#indent =縮排
        await ctx.send(f'set time to {time}')

    @commands.command()
    async def stop_task(self, ctx):
        task = self.bg_task   
        task.cancel()
        await ctx.send('task has been stopped.')

def setup(bot):
    bot.add_cog(Task(bot))
