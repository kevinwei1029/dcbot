import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import json, asyncio, datetime

with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

class Task(Cog_ext):
    def __init__(self, *args, **kwargs):#task初始化
        super().__init__(*args, **kwargs)#賦予classes的初始資料
        
        async def interval():
            await self.bot.wait_until_ready():


def setup(bot):
    bot.add_cog(Task(bot))