import discord
from discord.ext import commands, tasks
from core.classes import Cog_extension
import pymysql
import asyncio
import datetime
import json

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

class MyCog(Cog_extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel = 0
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @commands.command()
    async def set_channel(self, ctx, msg: int):
        self.channel = self.bot.get_channel(msg)
        await ctx.send(f"change to {self.channel.mention}")

    @tasks.loop(seconds=1.0)  # Run every second for accuracy
    async def printer(self):
        now = datetime.datetime.now()
        if now.minute % 5 == 0 and now.second == 0:  # At exact 5th, 10th, 15th, ... minute
            print(self.index)
            if self.index == 0:
                await self.send_message()
            await self.channel.send(self.index)
            self.index += 1

    async def send_message(self):
        self.channel = self.bot.get_channel(int(jdata["WELCOME"]))

    @printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(MyCog(bot))

#import discord
#from discord.ext import commands, tasks
#from core.classes import Cog_extension
#import pymysql
#import asyncio
#import datetime
#import json
#
#with open('setting.json', 'r', encoding='utf-8') as jfile:
#    jdata = json.load(jfile)
#
#class MyCog(Cog_extension):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.channel = 0
#        self.index = 0
#        self.printer.start()
#
#    def cog_unload(self):
#        self.printer.cancel()
#
#    @commands.command()
#    async def set_channel(self,ctx,msg:int):
#        self.channel = self.bot.get_channel(msg)
#        await ctx.send(f"change to {self.channel.mention}")
#
#
#    @tasks.loop(seconds=5.0)
#    async def printer(self):
#        print(self.index)
#        if(self.index==0):
#            await self.send_message()
#        await self.channel.send(self.index)
#        #await self.channel.send(self.index)
#        self.index += 1
#
#
#    async def send_message(self):
#        self.channel = self.bot.get_channel(int(jdata["WELCOME"]))
#
#    @printer.before_loop
#    async def before_printer(self):
#        print('waiting...')
#        await self.bot.wait_until_ready()
#
#async def setup(bot):
#    await bot.add_cog(MyCog(bot))



#class Task(Cog_extension):
#    def __init__(self,*args,**kwargs):
#        super().__init__(*args,**kwargs)
#
#        async def interval(self):
#            await self.bot.wait_until_ready()
#            self.channel = self.bot.get_channel(1137993729253318708)
#            while not self.bot.is_closed():
#                await self.channel.send("I'm running")
#                await asyncio.sleep(5)
#        self.bg_task = self.bot.loop.create_task(interval())
#

