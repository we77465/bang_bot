import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)
intents = discord.Intents.all()

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


import asyncio
async def main():
    for filename in  os.listdir("./cmds"):
        if filename.endswith("py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    await bot.start(jdata['TOKEN'])
if __name__=="__main__":
    asyncio.run(main())