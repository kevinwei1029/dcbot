import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import random
import json
import datetime

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
        laugh = ["w", "ww", "www",  "wwww", "wwwww", "xd", "xdd", "xddd", "xdddd", "xddddd", 
        "草", "笑", "kusa"]

        if msg.content == '水滴能做啥' or msg.content == '水滴能幹啥' or msg.content == '水滴能幹嘛':
            embed=discord.Embed(title="水滴能幹嘛", url="https://reurl.cc/NAXqLp", color=0x1E90FF, timestamp=datetime.datetime.now())
            embed.set_thumbnail(url="https://i.imgur.com/O6UbyuN.png")
            embed.add_field(name="水滴是誰 -", value="我不知道", inline=False)
            embed.add_field(name="水滴聊天 -", value="水滴能回覆的所有訊息", inline=False)
            embed.add_field(name="水滴指令 -", value="水滴能使用的指令", inline=False)
            embed.set_footer(text="看三小")
            await msg.channel.send(embed=embed)

        if msg.content == '水滴是誰':
            await msg.channel.send('一個有些怪功能的人工智障')

        if msg.content == '水滴聊天':
            await msg.channel.send('水滴會回答的話:\npeko, ahoy, 幹, 星爆, 閉嘴, 敲, 運勢, 機油, 舔嘴唇, 不要停下來')

        if msg.content == '水滴指令':
            embed=discord.Embed(title="水滴指令", url="https://reurl.cc/q5mWqg", color=0x1E90FF, timestamp=datetime.datetime.now())
            embed.add_field(name="^ping -", value="看現在的延遲", inline=False)
            embed.add_field(name="^n -", value="看n站(數字/a+畫師/c+角色/p+系列/t+標籤)", inline=False)
            embed.add_field(name="^p -", value="看p站(pid)", inline=False)
            embed.add_field(name="^圖片 -", value="隨機傳一張意義不明的圖", inline=False)
            embed.add_field(name="^botsay -", value="讓水滴複誦你說的話", inline=False)
            embed.add_field(name="^clean -", value="刪留言(刪n行)", inline=False)
            embed.set_footer(text="看三小")
            await msg.channel.send(embed=embed)

        if msg.content in b_word:
            await msg.channel.send('淦三小\n蛤')

        if msg.content == 'bot' or msg.content == '嗶嗶' or msg.content == '機油' or msg.content == '機器人':
            await msg.channel.send('嗶嗶.ㄐ...機油..好..難...喝')

        if msg.content in laugh:
            await msg.channel.send('笑屁')

        elif msg.content.endswith('peko') and msg.author != self.bot.user:
            await msg.channel.send('好油喔peko')

        elif msg.content.endswith('ahoy') and msg.author != self.bot.user:
            await msg.channel.send('Ahoy!')
        
        elif '舔' in msg.content or msg.content == '舔嘴唇' and msg.author != self.bot.user:
            await msg.channel.send('又舔! 又舔!! 又... 又舔嘴唇!!!')
            await msg.channel.send('https://memeprod.ap-south-1.linodeobjects.com/user-gif-post/1635254538236.gif')

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

        if msg.content == '3910U':
            await msg.channel.send("https://cdn.discordapp.com/attachments/966727218048925699/968675140583977040/360_20220427075337.png")

        if msg.content == '不要停下來' or "止まるんじゃねぇぞ" in msg.content:
            await msg.channel.send("止まるんじゃねぇぞ…\nₘₙⁿ\n▏n\n█▏　､⺍\n█▏ ⺰ʷʷｨ\n█◣▄██◣\n◥██████▋\n　◥████ █▎\n　　███▉ █▎\n　◢████◣⌠ₘ℩\n　　██◥█◣≫\n　　██　◥█◣\n　　█▉　　█▊\n　　█▊　　█▊\n　　█▊　　█▋\n　　 █▏　　█▙\n　　 █")

        if msg.content == '運勢':
            name = msg.author.name
            luck = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']
            color = ['紅色', '橙色', '檸檬黃', '蛋黃', '森林綠', '墨綠', '淺綠', '湖水藍', '淺藍','深靛', 
            '紫色', '黑色', '白色', '蛋白', '褐色', '粉紅', '藏青', '芒果青', '芭樂綠', '銀灰', 
            '皮膚色', '奶油色']
            emColor = [0x1E90FF, 0xff7575, 0x800080, 0x228B22, 0xE6D933, 0x696969, 0xBC8F8F, 0xD2691E, 0xF5F5F5, 0x39C5BB]
            ran_luck = random.choice(luck)
            ran_color = random.choice(color)
            ran_emColor = random.choice(emColor)
            num = random.randrange(1,100)

            embed=discord.Embed(title="抽到的運勢", color=ran_emColor)
            embed.set_author(name=name)
            embed.add_field(name="運氣:", value=ran_luck, inline=False)
            embed.add_field(name="幸運色:", value=ran_color, inline=False)
            embed.add_field(name="幸運數字:", value=num, inline=False)
            embed.set_footer(text="隨便亂做。僅供參考")
            await msg.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))