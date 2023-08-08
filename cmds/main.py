import discord
from discord.ext import commands
from core.classes import Cog_extension
import asyncio

class Main(Cog_extension):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)}(ms)')

async def setup(bot):
    await bot.add_cog(Main(bot))