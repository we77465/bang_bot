import discord
from discord.ext import commands

intents = discord.Intents.default()  # 获取默认的 intents 集合
intents.typing = False  # 关闭 typing 事件，可以根据你的需求进行调整
intents.members = True

bot = commands.Bot(command_prefix=']', intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    #https://discord.com/channels/1137958853502316636/1137993729253318708
    channel = bot.get_channel(1137993729253318708)
    print('f{member}in')
    await channel.send('f{member}hellooo')

@bot.event
async def on_member_remove(member):
    #https://discord.com/channels/1137958853502316636/1137993788955054180
    channel = bot.get_channel(1137993788955054180)
    print('f{member}out')
    await channel.send('f{member}byeeee')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f"!Hi <@{ctx.author.id}>")


bot.run('MTEzNzk1MjQwNDY4NDQxNTAyNg.GAQUHa.oSjlkE9lD8ikMMhFlmOgfwKB98vuzKDCQjHm-o')