import discord
from discord.ext import commands
from core.classes import Cog_extension
import asyncio

class Control(Cog_extension):
    def __init__(self,bot):
        self.bot = bot


    
#    @commands.command()
#    async def load(self,ctx,extension):
#        await self.bot.load_extension(f'cmds.{extension}')
#        await ctx.send(f'loading {extension} done')
#
#
#    @commands.command()
#    async def unload(self,ctx,extension):
#        await self.bot.unload_extension(f'cmds.{extension}')
#        await ctx.send(f'unloading {extension} done')
#
#
#    @commands.command()
#    async def reload(self,ctx,extension):
#        await self.bot.reload_extension(f'cmds.{extension}')
#        await ctx.send(f'reloading {extension} done')


async def setup(bot):
    await bot.add_cog(Control(bot))


# 這邊是broken的