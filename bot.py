import discord
from discord.ext import commands
import json
import os
import asyncio

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")


#@bot.command()
#async def load(ctx, cog_name):
#	try:
#		bot.load_extension(f'cogs.{cog_name}')
#	except:
#		await ctx.send('Failed.')
#		return
#	await ctx.send('load success!')
#
##這裡建個指令讓你可以卸載Cog
#@bot.command()
#async def unload(ctx, cog_name):
#	try:
#		bot.unload_extension(f'cogs.{cog_name}')
#	except:
#		await ctx.send('Failed.')
#		return
#	await ctx.send('unload success!')
#
##這裡建個指令讓你可以重新載入Cog
#@bot.command()
#async def reload(ctx, cog_name):
#	try:
#		bot.reload_extension(f'cogs.{cog_name}')
#	except:
#		await ctx.send('Failed.')
#		return
#	await ctx.send('reload success!')
#

async def main():
    for filename in  os.listdir("./cmds"):
        if filename.endswith("py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    await bot.start(jdata['TOKEN'])
if __name__=="__main__":
    
    asyncio.run(main())
    