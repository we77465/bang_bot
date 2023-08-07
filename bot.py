import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1137993729253318708)
    await channel.send(f'{member.name} hellooo')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1137993788955054180)
    await channel.send(f'{member.name} byeeee')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}(ms)')

bot.run('MTEzNzk1MjQwNDY4NDQxNTAyNg.GoiyXs.7lkE-K6PxOiVTnr5kOcdOyirmhWgrR3IMQFbAg')
