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
        channel = self.bot.get_channel(int(jdata['gen_channel']))
        await channel.send(f'歡迎 {member} 加入群組!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['gen_channel']))
        await channel.send(f'{member} 離開了群組, ㄅㄅ')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('別隨便創指令啊喂!!!')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('好像少了些東西喔?')
        else:
            await ctx.send("エロ発生。")

    #嗆人
    @commands.Cog.listener()
    async def on_message(self, msg):
        b_word = ["幹", "淦", "e04", "贛"]
        laugh = ["w", "ww", "www",  "wwww", "wwwww", "xd", "xdd", "xddd", "xdddd", "xddddd", 
        "草", "笑", "kusa"]
        laughSp = ["笑死", "咲死"]
        stan =["史丹利", "嗶嗶", "機油", "機器人"]
        nonstop = ["止まるんじゃねぇぞ", "不要停下來"]
        fbiword = ["Fbi", "fbi", "FBI", "羈押", "雞鴨", "緝押"]
        holdwo = ["修但幾勒", "修但幾類", "修蛋幾勒", "修蛋幾咧", "修但幾咧", "但勒", "但咧", "hold up"]

        if msg.content == '水滴能做啥' or msg.content == '水滴能幹啥' or msg.content == '水滴能幹嘛':
            embed=discord.Embed(title="水滴能幹嘛", url="https://reurl.cc/NAXqLp", color=0x1E90FF, timestamp=datetime.datetime.now())
            embed.set_thumbnail(url="https://i.imgur.com/O6UbyuN.png")
            embed.add_field(name="水滴是誰 -", value="我不知道", inline=False)
            embed.add_field(name="水滴聊天 -", value="水滴會回你話", inline=False)
            embed.add_field(name="水滴指令 -", value="水滴能使用的指令", inline=False)
            embed.set_footer(text="看三小")
            await msg.channel.send(embed=embed)

        if msg.content == '水滴是誰':
            await msg.channel.send('一個有些怪功能的人工智障')

        if msg.content == '水滴聊天':
            await msg.channel.send('<:water:972523626333077534><:water:972523626333077534><:water:972523626333077534><:water:972523626333077534><:water:972523626333077534>\n水滴會回答的話:\npeko, ahoy, 幹, 星爆, 閉嘴, 敲, 運勢, 機油, 舔嘴唇, 不要停下來, Fbi, www, 笑死, 修但幾咧, 好耶\n<:water:972523626333077534><:water:972523626333077534><:water:972523626333077534><:water:972523626333077534><:water:972523626333077534>')

        if msg.content == '水滴指令':
            embed=discord.Embed(title="水滴指令", url="https://reurl.cc/Dyyk2R", color=0x1E90FF, timestamp=datetime.datetime.now())
            embed.add_field(name="^ping -", value="看現在的延遲", inline=False)
            embed.add_field(name="^n -", value="看n站(n+數字/a+畫師/c+角色/p+系列/t+標籤)", inline=False)
            embed.add_field(name="^p -", value="看p站(pid)", inline=False)
            embed.add_field(name="^pic -", value="隨機傳一張意義不明的圖", inline=False)
            embed.add_field(name="^botsay -", value="讓水滴複誦你說的話", inline=False)
            embed.add_field(name="^clean -", value="刪留言(刪n行)", inline=False)
            embed.add_field(name="^talk -", value="講一些話", inline=False)
            embed.set_footer(text="看三小")
            await msg.channel.send(embed=embed)

        if msg.content in b_word and msg.author != self.bot.user:
            await msg.channel.send('淦三小\n蛤')

        if msg.content in stan and msg.author != self.bot.user:
            await msg.channel.send('嗶嗶.ㄐ...機油..好..難...喝')

        if msg.content in laugh:
            await msg.channel.send('笑屁喔 =.=')

        if msg.content in laughSp:
            await msg.channel.send('https://cdn.discordapp.com/attachments/966727218048925699/971689642351013948/IMG_7555.jpg')

        elif msg.content.endswith('peko') and msg.author != self.bot.user:
            await msg.channel.send('好油喔peko')

        elif msg.content.endswith('ahoy') and msg.author != self.bot.user:
            await msg.channel.send('Ahoy!')
        
        elif msg.content == '舔嘴唇' and msg.author != self.bot.user:
            await msg.channel.send('又舔! 又舔!! 又... 又舔嘴唇!!!')
            await msg.channel.send('https://cdn.discordapp.com/attachments/966727218048925699/971682963328733225/1635254538236.gif')

        elif '星爆' in msg.content and msg.author != self.bot.user:
            await msg.channel.send('你剛剛說了星爆對吧?')
            await msg.channel.send("https://cdn.discordapp.com/attachments/966727218048925699/971681509226446928/starburst.jpg")

        if msg.content == '閉嘴':
            await msg.channel.send("https://cdn.discordapp.com/attachments/966727218048925699/971681509935296542/376fce13dca941ba.gif")
        
        if msg.content == '敲' or msg.content == '不可以瑟瑟' or msg.content == '不可以色色':
            await msg.channel.send("https://cdn.discordapp.com/attachments/966727218048925699/971681509603958864/-.gif")

        if msg.content == '3910U':
            await msg.channel.send("https://cdn.discordapp.com/attachments/966727218048925699/968817594415083580/360_20220427181505.png")

        if msg.content in nonstop and msg.author != self.bot.user:
            await msg.channel.send("止まるんじゃねぇぞ…\nₘₙⁿ\n▏n\n█▏　､⺍\n█▏ ⺰ʷʷｨ\n█◣▄██◣\n◥██████▋\n　◥████ █▎\n　　███▉ █▎\n　◢████◣⌠ₘ℩\n　　██◥█◣≫\n　　██　◥█◣\n　　█▉　　█▊\n　　█▊　　█▊\n　　█▊　　█▋\n　　 █▏　　█▙\n　　 █")

        if msg.content == '運勢':
            name = msg.author.name
            luck = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']
            color = ['紅色', '橙色', '檸檬黃', '蛋黃', '森林綠', '墨綠', '淺綠', '湖水藍', '淺藍','深靛', 
            '紫色', '黑色', '白色', '蛋白', '褐色', '粉紅', '藏青', '芒果青', '芭樂綠', '銀灰', 
            '皮膚色', '奶油色', '紅豆紅', '亞麻色', '抽卡暴死的臉色', '彩虹', '玫瑰紅', '乳白色', '帽綠色']
            emColor = [0x1E90FF, 0xff7575, 0x800080, 0x228B22, 0xE6D933, 0x696969, 0xBC8F8F, 0xD2691E, 0xF5F5F5, 0x39C5BB]
            ran_luck = random.choice(luck)
            ran_color = random.choice(color)
            ran_emColor = random.choice(emColor)
            num = random.randrange(1,100)

            embed=discord.Embed(title="抽籤結果", color=ran_emColor)
            embed.set_author(name=name)
            embed.add_field(name="運勢:", value=ran_luck, inline=False)
            embed.add_field(name="幸運色:", value=ran_color, inline=False)
            embed.add_field(name="幸運數字:", value=num, inline=False)
            embed.set_footer(text="隨便亂做。僅供參考")
            await msg.channel.send(embed=embed)
        
        if msg.content in fbiword:
            Fbi = ["https://c.tenor.com/qEmU0G67ve4AAAAC/fbi-meme-fbi-open-up-memes.gif",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971687090473549834/IMG_7545.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971687090863616020/IMG_7547.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971687662954106900/IMG_7554.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971687670851985488/IMG_7553.gif",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971687691378917396/IMG_7551.webp",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971687691668316160/IMG_7550.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971687691919953990/IMG_7549.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971687692159037470/IMG_7548.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971825736530923570/D8042D41-6F89-4185-9211-3455974F0D5B.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/971825736782589972/F6724091-B209-4DAE-AEC4-C8329355F37C.jpg"]
            ranFbi = random.choice(Fbi)
            await msg.channel.send(ranFbi)

        if msg.content in holdwo:
            holdup = ["https://cdn.discordapp.com/attachments/966727218048925699/971825892462571600/IMG_7575.jpg", 
                      "https://cdn.discordapp.com/attachments/966727218048925699/971825892768759808/IMG_7574.jpg",
                      "https://cdn.discordapp.com/attachments/966727218048925699/971825893007827064/IMG_7573.jpg",
                      "https://cdn.discordapp.com/attachments/966727218048925699/971825893284642866/IMG_7572.jpg",
                      "https://cdn.discordapp.com/attachments/966727218048925699/971825893595050014/02E61B24-6844-4905-BD98-DA289BE5243C.jpg",
                      "https://cdn.discordapp.com/attachments/966727218048925699/971825893829914684/8183A61E-F12C-4251-BFC7-E09F23092DF9.jpg",
                      "https://cdn.discordapp.com/attachments/966727218048925699/971950343149731840/IMG_7578.png"]
            ranHold = random.choice(holdup)
            await msg.channel.send(ranHold)

        if msg.content == '好耶':
            yeah = ["https://cdn.discordapp.com/attachments/966727218048925699/972534736046157824/IMG_7617.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/972534736465567844/IMG_7616.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/972534736889217034/IMG_7615.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/972534737241505812/IMG_7614.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/972534737577074718/IMG_7613.png",
                    "https://cdn.discordapp.com/attachments/966727218048925699/972534738474639411/IMG_7612.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/972534738860519444/IMG_7611.jpg",
                    "https://cdn.discordapp.com/attachments/966727218048925699/972534739267375166/IMG_7610.webp"
                    ]  
            ranYeah = random.choice(yeah)
            await msg.channel.send(ranYeah)

def setup(bot):
    bot.add_cog(Event(bot))
