import discord
from discord.ext import commands
from core.classes import Cog_extension
import asyncio
import datetime
import pytz
import random

class Main(Cog_extension):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)}(ms)')

    @commands.command()
    async def em(self,ctx):
        current_time_utc = datetime.datetime.now()
        taipei_timezone = pytz.timezone('Asia/Taipei')
        current_time_taipei = current_time_utc.astimezone(taipei_timezone)
        embed=discord.Embed(title="we77465", url="https://pbs.twimg.com/media/E4VHyPEVgAQHrgi?format=jpg&name=small", description="weee",timestamp=current_time_taipei)
        embed.set_author(name="we77465", url="https://github.com/we77465", icon_url="https://pbs.twimg.com/media/E4VHyPEVgAQHrgi?format=jpg&name=small")
        embed.set_thumbnail(url="https://pbs.twimg.com/media/E4VHyPEVgAQHrgi?format=jpg&name=small")
        embed.add_field(name="emm", value="你啥", inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def said(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def online(self,ctx):
        all_online = []
        for men in ctx.guild.members:
            #await ctx.send(f"{men} {men.status}")
            if(str(men.status)=="online" and men.bot==False):
                all_online.append(men.name)
        await ctx.send(all_online)
        random_online = random.sample(all_online,k=2)

    
    @commands.command()
    async def clean(self,ctx,num:int):
        num+=1
        await ctx.channel.purge(limit=num)


async def setup(bot):
    await bot.add_cog(Main(bot))