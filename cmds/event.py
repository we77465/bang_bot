import discord
from discord.ext import commands
from core.classes import Cog_extension
import random
import json
import re
import requests

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


    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.author == self.bot.user:
            return
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        if url_pattern.search(msg.content):
            await msg.channel.send(f'{msg.author.mention} 訊息包含 URL。')
            key = jdata["OpenAI_key"]
            response = requests.post(
                'https://api.openai.com/v1/completions',
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {key}'
                },
                json = {
                    'model': 'text-davinci-003',
                    'prompt': f'{msg.content}這段文字中 哪段是url 並回傳並且不要打其他任何字',
                    'temperature': 0.4,
                    'max_tokens': 300
                }
            )
            json = response.json()
            #await msg.channel.send(response.text)
            #await msg.channel.send(response.status_code)
            await msg.channel.send(json['choices'][0]['text'])

            

async def setup(bot):
    await bot.add_cog(Events(bot))