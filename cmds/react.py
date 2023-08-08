import discord
from discord.ext import commands
from core.classes import Cog_extension
import random
import json
with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

class React(Cog_extension):
   


    @commands.command()
    async def hello(self,ctx):
        await ctx.send(f"!Hi <@{ctx.author.id}>")

    @commands.command()
    async def 圖片(self,ctx):
        pic = discord.File(jdata['pic'][0])
        await ctx.send(file=pic)

    @commands.command()
    async def 隨機(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def url(self,ctx):
        pic = jdata['url_pic']
        await ctx.send(pic)


async def setup(bot):
    await bot.add_cog(React(bot))