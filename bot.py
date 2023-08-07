import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["WELCOME"]))
    await channel.send(f'{member.name} hellooo')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["LEAVE"]))
    await channel.send(f'{member.name} byeeee')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}(ms)')

@bot.command()
async def hello(ctx):
    await ctx.send(f"!Hi <@{ctx.author.id}>")


bot.run(jdata['TOKEN'])
