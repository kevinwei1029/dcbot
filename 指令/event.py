import discord
from discord.ext import commands
from 核心.classes import Cog_ext
import random
import json
import datetime

with open('setting.json', mode='r', encoding='utf8') as jfile:  #'r'=read(讀取)
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

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        if str(data.emoji) == "➕":
            guild = self.bot.get_guild(data.guild_id)
            role = guild.get_role(988483240136409189)
            await data.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        if str(data.emoji) == "➕":
            guild = self.bot.get_guild(data.guild_id)
            user = guild.get_member(data.user_id)
            role = guild.get_role(988483240136409189)
            await user.remove_roles(role)

    #聊天
    @commands.Cog.listener()
    async def on_message(self, msg):
        b_word = ["幹", "淦", "e04", "贛"]
        laugh = [
            "w", "ww", "www", "wwww", "wwwww", "xd", "xdd", "xddd", "xdddd",
            "xddddd", "草", "笑", "kusa", "くさ"
        ]
        laughSp = ["笑死", "咲死"]
        stan = ["史丹利", "嗶嗶", "機油", "機器人"]
        nonstop = ["止まるんじゃねぇぞ", "不要停下來"]
        fbiword = ["Fbi", "fbi", "FBI", "羈押", "雞鴨", "緝押"]
        holdwo = [
            "修但幾勒", "修但幾類", "修蛋幾勒", "修蛋幾咧", "修但幾咧", "但勒", "但咧", "hold up"
        ]
        youtube = [
            "<:youtube:972831278632149052>",
            "<:youtube_old:972831218477453365>"
        ]
        donkno = ["窩不知道", "我不知道", "不知道", "不知", "嗯災", "啊災"]
        dot = [
            "......", ".....", "....", "...", "..", ".", "……", "…..", "….", "…"
        ]

        if msg.content == '身分加加':
            await msg.delete()
            await msg.channel.send("按➕獲取好像有點用的新人身分組")
            
        if msg.content == "按➕獲取好像有點用的新人身分組" and msg.author == self.bot.user:
            await msg.add_reaction("➕")

        if msg.content == '水滴能做啥' or msg.content == '水滴能幹啥' or msg.content == '水滴能幹嘛':
            embed = discord.Embed(title="水滴能幹嘛",
                                  url="https://reurl.cc/NAXqLp",
                                  color=0x1E90FF,
                                  timestamp=datetime.datetime.now())
            embed.set_thumbnail(url="https://i.imgur.com/O6UbyuN.png")
            embed.add_field(name="水滴是誰 -", value="我不知道", inline=False)
            embed.add_field(name="水滴聊天 -", value="水滴會回你話", inline=False)
            embed.add_field(name="水滴指令 -", value="水滴能使用的指令", inline=False)
            embed.set_footer(text="看三小")
            await msg.channel.send(embed=embed)

        if msg.content == '水滴是誰':
            await msg.channel.send('一個有些怪功能的人工智障')

        if msg.content == '水滴聊天':
            await msg.channel.send(
                '<:water:972523626333077534><:water:972523626333077534><:water:972523626333077534><:water:972523626333077534><:water:972523626333077534>\n水滴會回答的話:\npeko, ahoy, 幹, 星爆, 閉嘴, 敲, 運勢, 機油, 舔嘴唇, 不要停下來, Fbi, www, 笑死, 修但幾咧, 好耶, 點你媽, 確實, 我不知道, 嗨, 嗆, ㄏ, 度的 和其他怪怪的東西\n<:water:972523626333077534><:water:972523626333077534><:water:972523626333077534><:water:972523626333077534><:water:972523626333077534>'
            )

        if msg.content == '水滴指令':
            embed = discord.Embed(title="水滴指令",
                                  url="https://reurl.cc/Dyyk2R",
                                  color=0x1E90FF,
                                  timestamp=datetime.datetime.now())
            embed.add_field(name="^ping -", value="看現在的延遲", inline=False)
            embed.add_field(name="^n -", value="看n站(+神的語言)", inline=False)
            embed.add_field(name="^p -", value="看p站(+pid)", inline=False)
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
            await msg.channel.send(
                'https://cdn.discordapp.com/attachments/966727218048925699/971689642351013948/IMG_7555.jpg'
            )

        elif msg.content.endswith('peko') and msg.author != self.bot.user:
            await msg.channel.send('好油喔peko')

        elif msg.content.endswith('ahoy') and msg.author != self.bot.user:
            await msg.channel.send('Ahoy!')

        elif msg.content == '舔嘴唇' and msg.author != self.bot.user:
            await msg.channel.send('又舔! 又舔!! 又... 又舔嘴唇!!!')
            await msg.channel.send(
                'https://cdn.discordapp.com/attachments/966727218048925699/971682963328733225/1635254538236.gif'
            )

        elif '星爆' in msg.content and msg.author != self.bot.user:
            await msg.channel.send('你剛剛說了星爆對吧?')
            await msg.channel.send(
                "https://cdn.discordapp.com/attachments/966727218048925699/971681509226446928/starburst.jpg"
            )

        if msg.content == '閉嘴':
            await msg.channel.send(
                "https://cdn.discordapp.com/attachments/966727218048925699/971681509935296542/376fce13dca941ba.gif"
            )

        if msg.content == '敲' or msg.content == '不可以瑟瑟' or msg.content == '不可以色色':
            await msg.channel.send(
                "https://cdn.discordapp.com/attachments/966727218048925699/971681509603958864/-.gif"
            )

        if msg.content == '3910U':
            await msg.channel.send(
                "https://cdn.discordapp.com/attachments/966727218048925699/968817594415083580/360_20220427181505.png"
            )

        if msg.content in nonstop and msg.author != self.bot.user:
            await msg.channel.send(
                "止まるんじゃねぇぞ…\nₘₙⁿ\n▏n\n█▏　､⺍\n█▏ ⺰ʷʷｨ\n█◣▄██◣\n◥██████▋\n　◥████ █▎\n　　███▉ █▎\n　◢████◣⌠ₘ℩\n　　██◥█◣≫\n　　██　◥█◣\n　　█▉　　█▊\n　　█▊　　█▊\n　　█▊　　█▋\n　　 █▏　　█▙\n　　 █"
            )

        if msg.content == '運勢':
            name = msg.author.name
            luck = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']
            color = [
                '紅色', '橙色', '檸檬黃', '蛋黃', '森林綠', '墨綠', '淺綠', '湖水藍', '淺藍', '深靛',
                '紫色', '黑色', '白色', '蛋白', '褐色', '粉紅', '藏青', '芒果青', '芭樂綠', '銀灰',
                '皮膚色', '奶油色', '紅豆紅', '亞麻色', '抽卡暴死的臉色', '彩虹', '玫瑰紅', '乳白色',
                '帽綠色', '煎餃色', '綠一色'
            ]
            emColor = [
                0x1E90FF, 0xff7575, 0x800080, 0x228B22, 0xE6D933, 0x696969,
                0xBC8F8F, 0xD2691E, 0xF5F5F5, 0x39C5BB
            ]
            ran_luck = random.choice(luck)
            ran_color = random.choice(color)
            ran_emColor = random.choice(emColor)
            num = random.randrange(1, 100)

            embed = discord.Embed(title="抽籤結果", color=ran_emColor)
            embed.set_author(name=name)
            embed.add_field(name="運勢:", value=ran_luck, inline=False)
            embed.add_field(name="幸運色:", value=ran_color, inline=False)
            embed.add_field(name="幸運數字:", value=num, inline=False)
            embed.set_footer(text="隨便亂做。僅供參考")
            await msg.channel.send(embed=embed)

        if msg.content in fbiword:
            Fbi = [
                "https://c.tenor.com/qEmU0G67ve4AAAAC/fbi-meme-fbi-open-up-memes.gif",
                "https://cdn.discordapp.com/attachments/966727218048925699/971687090473549834/IMG_7545.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971687662954106900/IMG_7554.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971687670851985488/IMG_7553.gif",
                "https://cdn.discordapp.com/attachments/966727218048925699/971687691378917396/IMG_7551.webp",
                "https://cdn.discordapp.com/attachments/966727218048925699/971687691668316160/IMG_7550.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971687691919953990/IMG_7549.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971687692159037470/IMG_7548.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971825736530923570/D8042D41-6F89-4185-9211-3455974F0D5B.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971825736782589972/F6724091-B209-4DAE-AEC4-C8329355F37C.jpg"
            ]
            ranFbi = random.choice(Fbi)
            await msg.channel.send(ranFbi)

        if msg.content in holdwo:
            holdup = [
                "https://cdn.discordapp.com/attachments/966727218048925699/971825892462571600/IMG_7575.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971825892768759808/IMG_7574.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971825893007827064/IMG_7573.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971825893284642866/IMG_7572.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971825893595050014/02E61B24-6844-4905-BD98-DA289BE5243C.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971825893829914684/8183A61E-F12C-4251-BFC7-E09F23092DF9.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/971950343149731840/IMG_7578.png",
                "https://cdn.discordapp.com/attachments/967361900247674880/979044769957310464/IMG_8352.jpg"
            ]
            ranHold = random.choice(holdup)
            await msg.channel.send(ranHold)

        if msg.content == '好耶':
            yeah = [
                "https://cdn.discordapp.com/attachments/966727218048925699/972534736046157824/IMG_7617.jpg",
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

        if 'twitter.com' in msg.content and msg.author.id == 682823490927329307:
            await msg.add_reaction("<:twitter:972831142094987335>")

        if 'nhentai.net' in msg.content and msg.author.id == 682823490927329307:
            await msg.add_reaction("<:nhentai:972833833680502825>")

        if 'www.youtube.com' in msg.content and msg.author.id == 682823490927329307:
            ranyt = random.choice(youtube)
            await msg.add_reaction(ranyt)

        elif 'youtu.be' in msg.content and msg.author.id == 682823490927329307:
            ranyt = random.choice(youtube)
            await msg.add_reaction(ranyt)

        if 'pixiv.net' in msg.content and msg.author.id == 682823490927329307:
            await msg.add_reaction("<:pixiv:972831041284882502>")

        if 'gamer.com.tw' in msg.content and msg.author.id == 682823490927329307:
            await msg.add_reaction("<:bahamut:972831085308293231>")

        if msg.content == '雀食' or msg.content == '確實':
            right = [
                "https://cdn.discordapp.com/attachments/966727218048925699/972897997224542278/IMG_7657.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/972897997430071326/IMG_7656.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/972897997664968724/IMG_7655.png",
                "https://cdn.discordapp.com/attachments/966727218048925699/972897997878870116/IMG_7654.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/972897998109560902/IMG_7653.png",
                "https://cdn.discordapp.com/attachments/966727218048925699/972897998344429638/IMG_7652.webp",
                "https://cdn.discordapp.com/attachments/966727218048925699/972897998570946600/IMG_7651.jpg"
            ]
            ranri = random.choice(right)
            await msg.channel.send(ranri)

        if msg.content in dot and msg.author != self.bot.user:
            await msg.channel.send("點你媽。")

        if msg.content in donkno:
            know = [
                "https://cdn.discordapp.com/attachments/966727218048925699/973266858688016444/IMG_7676.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/973266858939645982/IMG_7675.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/973266859140993034/IMG_7674.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/973266859354914848/IMG_7673.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/973266859564625960/IMG_7672.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/973266859807879199/IMG_7671.jpg",
                "https://cdn.discordapp.com/attachments/967070448149991434/977944835606593536/a32d78dbaf69a87c.png"
            ]
            rankn = random.choice(know)
            await msg.channel.send(rankn)

        if msg.content == "嗨":
            await msg.channel.send(f"嗨，{msg.author.mention}")

        if msg.content in ["pop", "泡泡"] and msg.author != self.bot.user:
            await msg.channel.send(
                "給你owo/\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||"
            )

        if '嗆' in msg.content and '@' in msg.content and msg.author != self.bot.user:
            if msg.mentions[0].id == 885360032852627477 or msg.mentions[
                    0].id == 703783011761782954:
                await msg.channel.send("給我打松煙32。")
            elif msg.mentions[0].id == 681076728465981450:
                await msg.channel.send("不要\n這位越嗆會越興奮")
            else:
                await msg.channel.send("這還有嗆的必要嗎?")

        if msg.content in ["ㄏㄏ", "ㄏ"] and msg.author != self.bot.user:
            await msg.channel.send("ㄏ你老母")

        if msg.content in ["度", "對", "沒錯", "度的", "對的", "是", "是的"
                           ] and msg.author != self.bot.user:
            await msg.channel.send("度的owo")

        if msg.content in ["怕", "怕爆", "怕豹"]:
            pa = [
                "https://cdn.discordapp.com/attachments/967361900247674880/978322433205497866/IMG_8026.png",
                "https://cdn.discordapp.com/attachments/967361900247674880/978322433490690068/IMG_8024.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978322433729781820/IMG_8023.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978322434006601798/IMG_8022.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978322434270822470/IMG_8021.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978322434795130990/IMG_8019.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978325066452451418/3.gif"
            ]
            ranpa = random.choice(pa)
            await msg.channel.send(ranpa)

        if msg.content in ["沒有", "並沒有"]:
            nope = [
                "https://cdn.discordapp.com/attachments/966727218048925699/978330979523502140/IMG_8046.jpg",
                "https://cdn.discordapp.com/attachments/966727218048925699/978330979825512508/IMG_8045.jpg"
            ]
            rnope = random.choice(nope)
            await msg.channel.send(rnope)

        if msg.content in ["歐", "歐洲", "歐氣", "歐洲人"]:
            europe = [
                "https://cdn.discordapp.com/attachments/967361900247674880/978579737054183435/IMG_8139.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579737268088902/IMG_8134.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579737528127498/IMG_8130.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579737775583262/IMG_8129.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579738119528469/IMG_8132.png",
                "https://cdn.discordapp.com/attachments/967361900247674880/978581657479176232/IMG_8142.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978581657756008488/IMG_8141.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978581657999274024/A80B70C7-30F2-497D-AA97-0773FF723C14.png"
            ]
            raeu = random.choice(europe)
            await msg.channel.send(raeu)

        if msg.content in ["非", "非洲", "非氣", "非洲人"]:
            africa = [
                "https://cdn.discordapp.com/attachments/967361900247674880/978579794562265118/IMG_8140.png",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579794763599872/IMG_8138.png",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579795053010964/IMG_8137.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579795317227592/IMG_8135.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579795531149342/IMG_8136.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579795715715092/IMG_8133.jpg",
                "https://cdn.discordapp.com/attachments/967361900247674880/978579795946397737/IMG_8131.png",
                "https://cdn.discordapp.com/attachments/967361900247674880/981245940180615178/19D28D9A-4B06-4CF2-BFE6-C2D48DFF1DC5.png"
            ]
            raaf = random.choice(africa)
            await msg.channel.send(raaf)

        if msg.content == "隨便抽":
            lottery = ["<:en:978708709553340456>", "<:esr:978708903317614683>", "<:eur:978711217088626709>"]
            rate = [30, 15, 5]
            rl = random.choices(lottery, weights=rate, k=10)
            await msg.channel.send(f'{rl[0]}{rl[1]}{rl[2]}{rl[3]}{rl[4]}\n{rl[5]}{rl[6]}{rl[7]}{rl[8]}{rl[9]}')

        if msg.content == "隨便百抽":
            lottery = ["<:en:978708709553340456>", "<:esr:978708903317614683>", "<:eur:978711217088626709>"]
            rate = [30, 15, 5]
            rl = random.choices(lottery, weights=rate, k=100)
            n = 0
            sr = 0
            ur = 0
            for i in range(100):
                if rl[i] == "<:en:978708709553340456>":
                    n = n+1
                elif rl[i] == "<:esr:978708903317614683>":
                    sr = sr+1
                elif rl[i] == "<:eur:978711217088626709>":
                    ur = ur+1
            await msg.channel.send(f"<:eur:978711217088626709>: {ur}個\n<:esr:978708903317614683>: {sr}個\n<:en:978708709553340456>: {n}個")

        if msg.content == "日麻抽":
            majong = ["<:1m:990537992416428062>",
            "<:2m:990538050058731522>",
            "<:3m:990538090009464862>",
            "<:4m:990538129645654027>",
            "<:5mr:990538212156014612>",
            "<:6m:990538338119319622>",
            "<:7m:990538388413231134>",
            "<:8m:990538429794246696>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5pr:990539005798014986>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5sr:990540451222274118>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>",
            "<:1m:990537992416428062>",
            "<:2m:990538050058731522>",
            "<:3m:990538090009464862>",
            "<:4m:990538129645654027>",
            "<:5m:990538166127718432>",
            "<:6m:990538338119319622>",
            "<:7m:990538388413231134>",
            "<:8m:990538429794246696>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>",
            "<:1m:990537992416428062>",
            "<:2m:990538050058731522>",
            "<:3m:990538090009464862>",
            "<:4m:990538129645654027>",
            "<:5m:990538166127718432>",
            "<:6m:990538338119319622>",
            "<:7m:990538388413231134>",
            "<:8m:990538429794246696>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>",
            "<:1m:990537992416428062>",
            "<:2m:990538050058731522>",
            "<:3m:990538090009464862>",
            "<:4m:990538129645654027>",
            "<:5m:990538166127718432>",
            "<:6m:990538338119319622>",
            "<:7m:990538388413231134>",
            "<:8m:990538429794246696>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>"
            ]
            r = random.sample(majong, 14)
            doro = r[13]
            r.remove(r[13])
            rs = sorted(r, key= lambda x: x[-15:])
            await msg.channel.send(f'{rs[0]}{rs[1]}{rs[2]}{rs[3]}{rs[4]}{rs[5]}{rs[6]}{rs[7]}{rs[8]}{rs[9]}{rs[10]}{rs[11]}{rs[12]} {doro}')

        if msg.content == "台麻抽" or msg.content == "臺麻抽":
            majong = ["<:1m:990537992416428062>",
            "<:2m:990538050058731522>",
            "<:3m:990538090009464862>",
            "<:4m:990538129645654027>",
            "<:5m:990538166127718432>",
            "<:6m:990538338119319622>",
            "<:7m:990538388413231134>",
            "<:8m:990538429794246696>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>",
            "<:1m:990537992416428062>",
            "<:2m:990538050058731522>",
            "<:3m:990538090009464862>",
            "<:4m:990538129645654027>",
            "<:5m:990538166127718432>",
            "<:6m:990538338119319622>",
            "<:7m:990538388413231134>",
            "<:8m:990538429794246696>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>",
            "<:1m:990537992416428062>",
            "<:2m:990538050058731522>",
            "<:3m:990538090009464862>",
            "<:4m:990538129645654027>",
            "<:5m:990538166127718432>",
            "<:6m:990538338119319622>",
            "<:7m:990538388413231134>",
            "<:8m:990538429794246696>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>",
            "<:1m:990537992416428062>",
            "<:2m:990538050058731522>",
            "<:3m:990538090009464862>",
            "<:4m:990538129645654027>",
            "<:5m:990538166127718432>",
            "<:6m:990538338119319622>",
            "<:7m:990538388413231134>",
            "<:8m:990538429794246696>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>"
            ]
            r = random.sample(majong, 17)
            doro = r[16]
            r.remove(r[16])
            rs = sorted(r, key= lambda x: x[-15:])
            await msg.channel.send(f'{rs[0]}{rs[1]}{rs[2]}{rs[3]}{rs[4]}{rs[5]}{rs[6]}{rs[7]}{rs[8]}{rs[9]}{rs[10]}{rs[11]}{rs[12]}{rs[13]}{rs[14]}{rs[15]} {doro}')

        if msg.content == "三麻抽":
            majong = ["<:1m:990537992416428062>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5pr:990539005798014986>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5sr:990540451222274118>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>",
            "<:1m:990537992416428062>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>",
            "<:1m:990537992416428062>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>",
            "<:1m:990537992416428062>",
            "<:9m:990538471535955968>",
            "<:1p:990538754718576690>",
            "<:2p:990538805968777236>",
            "<:3p:990538855679664178>",
            '<:4p:990538903230496768>',
            "<:5p:990538958645624863>",
            "<:6p:990539124987535360>",
            "<:7p:990539162694352900>",
            "<:8p:990539202749935686>",
            "<:9p:990539246240694292>",
            "<:1s:990539353476452373>",
            "<:2s:990539390684119070>",
            "<:3s:990539435626074112>",
            "<:4s:990539492727341126>",
            "<:5s:990540390534905916>",
            "<:6s:990540542880415785>",
            "<:7s:990540604331155517>",
            "<:8s:990540683968405504>",
            "<:9s:990540891947163678>",
            "<:east:990540941695799337>", 
            "<:south:990540993721942016>", 
            "<:west:990541034998071317>", 
            "<:north:990541077633187890>", 
            "<:white:990541114123616306>", 
            "<:fa:990541151939461212>", 
            "<:zh:990541184575352913>"
            ]
            r = random.sample(majong, 14)
            doro = r[13]
            r.remove(r[13])
            rs = sorted(r, key= lambda x: x[-15:])
            await msg.channel.send(f'{rs[0]}{rs[1]}{rs[2]}{rs[3]}{rs[4]}{rs[5]}{rs[6]}{rs[7]}{rs[8]}{rs[9]}{rs[10]}{rs[11]}{rs[12]} {doro}')  

        if msg.content == '婆':
            await msg.channel.send("醒")

        if msg.content == '迎新':
            new = ["https://cdn.discordapp.com/attachments/420555023844507661/780761251944333322/f2426bc00e7babc1.png",
                    "https://cdn.discordapp.com/attachments/966718811791315016/979746969268387860/4cb447ff07aee6e1-1.jpg"]
            rannew = random.choice(new) 
            await msg.channel.send(rannew)  

        


def setup(bot):
    bot.add_cog(Event(bot))
