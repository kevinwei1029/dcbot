import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import random
import json

with open('setting.json', mode='r', encoding='utf8') as jfile: #'r'=read(讀取)
    jdata = json.load(jfile)

class Event(Cog_ext):
    
    #有人加入/退出群組
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Test_gen_channel']))
        await channel.send(f'歡迎 {member} 加入群組!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Test_gen_channel']))
        await channel.send(f'{member} 離開了群組')

    #嗆人
    @commands.Cog.listener()
    async def on_message(self, msg):
        b_word = ["幹", "淦", "e04", "贛"]
        pic = discord.File("C:\\Users\\miran\\OneDrive\\桌面\\DD\\python\\dcbot\\圖片\\starburst.jpg")
        if msg.content in b_word:
            await msg.channel.send('淦三小\n蛤')

        elif msg.content.endswith('peko') and msg.author != self.bot.user:
            await msg.channel.send('好油喔peko')
        
        elif '星爆' in msg.content and msg.author != self.bot.user:
            await msg.channel.send('你剛剛說了星爆對吧?')
            await msg.channel.send(file = pic)

def setup(bot):
    bot.add_cog(Event(bot))