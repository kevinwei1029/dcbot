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

        if msg.content == '水滴能做啥' or msg.content == '水滴能幹啥':
            await msg.channel.send('水滴聊天 - 水滴能回覆的所有訊息\n水滴指令 - 水滴能使用的指令')
        if msg.content == '水滴是誰':
            await msg.channel.send('一個有些怪功能的人工智障')
        if msg.content == '水滴聊天':
            await msg.channel.send('星爆, peko, 幹, 閉嘴, 敲, 運勢')
        if msg.content == '水滴指令':
            await msg.channel.send('^ping - 給你現在的延遲\n^n+數字 - 給你n站的網址\n^p+數字 - 給你pixiv的網址')

        if msg.content in b_word:
            await msg.channel.send('淦三小\n蛤')

        elif msg.content.endswith('peko') and msg.author != self.bot.user:
            await msg.channel.send('好油喔peko')
        
        elif '星爆' in msg.content and msg.author != self.bot.user:
            pic = discord.File("C:\\Users\\miran\\OneDrive\\桌面\\DD\\python\\dcbot\\圖片\\starburst.jpg")
            await msg.channel.send('你剛剛說了星爆對吧?')
            await msg.channel.send(file = pic)

        if msg.content == '閉嘴':
            pic = discord.File("C:\\Users\\miran\\OneDrive\\桌面\\DD\\python\\dcbot\\圖片\\閉嘴.gif")
            await msg.channel.send(file = pic)
        
        if msg.content == '敲' or msg.content == '不可以瑟瑟' or msg.content == '不可以色色':
            pic = discord.File("C:\\Users\\miran\\OneDrive\\桌面\\DD\\python\\dcbot\\圖片\\不可以瑟瑟-敲.gif")
            await msg.channel.send(file = pic)

        if msg.content == '運勢':
            name = msg.author.name
            luck = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']
            color = ['紅', '橙', '黃', '綠', '藍', '靛', '紫', '黑', '白', '褐']
            ran_luck = random.choice(luck)
            ran_color = random.choice(color)
            num = random.randrange(1,100)

            embed=discord.Embed(title="抽到的運勢", color=0xff7575)
            embed.set_author(name=name)
            embed.add_field(name="運氣:", value=ran_luck, inline=False)
            embed.add_field(name="幸運色:", value=ran_color, inline=False)
            embed.add_field(name="幸運數字:", value=int(num), inline=False)
            embed.set_footer(text="隨便亂做。僅供參考")
            await msg.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))