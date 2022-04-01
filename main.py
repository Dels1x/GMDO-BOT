import discord
import os
from discord.ext import commands


token = os.environ['bot_token']

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix='?')



@bot.event
async def on_ready():
    print('Bot is online.')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_member_join(member: discord.Member):
    emojis = {e.name: str(e) for e in bot.emojis}
    channel = bot.get_channel(886678202129448972)
    await channel.send(f"К нам присоединился {member.mention}! {emojis['owner']}Добро пожаловать в GMD | Общений!"
             f" Теперь нас {len(member.guild.members)}! {emojis['EBATB']}")


@bot.event
async def on_member_remove(member: discord.Member):
    emojis = {e.name: str(e) for e in bot.emojis}
    channel = bot.get_channel(886678202129448972)
    await channel.send(f"{member} сбежал с сервера! {emojis['GRUST']}")


bot.run(token)
