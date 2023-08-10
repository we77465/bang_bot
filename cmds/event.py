import discord
from discord.ext import commands
from core.classes import Cog_extension
import random
import json
with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

class Events(Cog_extension):
   

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata["WELCOME"]))
        await channel.send(f'{member.name} hellooo')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata["LEAVE"]))
        await channel.send(f'{member.name} byeeee')

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content=='bang' and msg.author!=self.bot.user:
            await msg.channel.send('banggg')

async def setup(bot):
    await bot.add_cog(Events(bot))