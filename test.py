import discord
from discord.ext import commands

intents = discord.Intents.all()


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online. Logged in as {bot.user.name} - {bot.user.id}")

@bot.command()
async def ping(ctx):
    """回应 'ping' 命令，显示机器人延迟"""
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

@bot.command()
async def hello(ctx):
    """回应 'hello' 命令，欢迎用户"""
    await ctx.send(f"Hello, {ctx.author.mention}!")

@bot.command()
async def 圖片(ctx):
    pic = discord.File('C:\\Users\\kenan\\Desktop\\school\\bang_bot\\bang_bot\\pic\\下載.png')
    await ctx.send(file=pic)

bot.run('MTEzNzk1MjQwNDY4NDQxNTAyNg.GAQUHa.oSjlkE9lD8ikMMhFlmOgfwKB98vuzKDCQjHm-o')
