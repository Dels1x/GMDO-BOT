import discord
from discord.ext import commands
import asyncio
import random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun cog loaded')

    @commands.command(aliases=['ОВНЕР', "Овнер", "овнер"])
    async def owner(self, ctx):
        emojis = {e.name: str(e) for e in ctx.bot.emojis}
        role = discord.utils.get(ctx.author.guild.roles, name="ОВНЕР")
        await ctx.send(
            f"<@{ctx.author.id}>, здравствуй {emojis['__']}! Че ещё хочешь? Завтра пройдёт раздача чмовнера! Что? По еблищу,"
            f" не? Стяни пиздак, пожалуйста, раздача прошла 2 дня назад. Доброго дня! {emojis['KRUT']}"
            f"Да ладно тебе. Поплачь об этом! {emojis['XAPOW']} Пока чмодерация отдыхает, я разыграл конкурс на овнера."
            f" Им стал... <@{ctx.author.id}>! Поздравляю! {emojis['POZDRAVLYAU']}"
        )
        await ctx.author.add_roles(role)
        await asyncio.sleep(10)
        await ctx.author.remove_roles(role)

    @commands.command(aliases=["нг", "Нг", "НГ", "нГ", "новыйгод", "НОВЫЙГОД", "Новыйгод", "НовыйГод", "NG", "Ng", "nG"])
    async def ng(self, ctx):
      year = random.randint(0, 366)
      if year == 366:
        await ctx.send(f"Новый год не наступит НИКОГДА!")
      else:
        await ctx.send(f"Новый год наступит через {year} дней!")

    @commands.command(aliases=["WANTED", "wANTED","Wanted"])
    async def wanted(self, ctx, user: discord.Member = None):
      if user == None:
        user = ctx.author
      wanted = Image.open('wanted.jpg')
      avatar = user.avatar_url_as(size=128)
      avt = BytesIO(await avatar.read())
      img = Image.open(avt)
      img = img.resize((310, 310))
       
      wanted.paste(img, (80, 220))
      wanted.save("new_wanted.jpg", "JPEG")
      await ctx.send(file=discord.File("new_wanted.jpg"))

    @commands.command(aliases=["флипи", "ФЛИПИ", "Флипи", "фЛИПИ", "FLIPY", "fLIPY", "Flipy", "FliPy"])
    async def flipy(self, ctx, user: discord.Member = None):
      if user == None:
        user = ctx.author
      flipy = Image.open("flipy.jpg")
      avatar = user.avatar_url_as(size=256)
      avt = BytesIO(await avatar.read())
      img = Image.open(avt)
      img = img.resize((200, 200))

      flipy.paste(img, (22, 22))
      canvas = ImageDraw.Draw(flipy)
      headline = ImageFont.truetype('arial_bold.ttf', size=33)
      canvas.text((256, 115),
                  f"{user.name}  [300м от Вас]",
                  font=headline,
                  fill="#1E651F")
      flipy.save("new_flipy.jpg", "JPEG")
      await ctx.send(file=discord.File("new_flipy.jpg"))


    @commands.command(aliases=["флипи2", "ФЛИПИ2", "Флипи2", "фЛИПИ2", "FLIPY2", "fLIPY2", "Flipy2", "FliPy2"])
    async def flipy2(self, ctx, *, name: str = ""):
      flipy = Image.open("flipy.jpg")
      url = ctx.message.attachments[0].url
      response = requests.get(url, stream=True).raw
      img = Image.open(response)
      img = img.resize((200, 200))

      flipy.paste(img, (22, 22))
      canvas = ImageDraw.Draw(flipy)
      headline = ImageFont.truetype('arial_bold.ttf', size=33)
      canvas.text((256, 115),
                  f"{name}  [300м от Вас]",
                  font=headline,
                  fill="#1E651F")
      flipy.save("new_flipy2.jpg", "JPEG")
      await ctx.send(file=discord.File("new_flipy2.jpg"))


def setup(bot):
    bot.add_cog(Fun(bot))
