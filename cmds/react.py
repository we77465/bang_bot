import discord
from discord.ext import commands
from core.classes import Cog_extension
import random
import json
import requests


with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)

class React(Cog_extension):
   

    @commands.command()
    async def GPT(self,ctx,*,msg):
        key = jdata["OpenAI_key"]
        response = requests.post(
             'https://api.openai.com/v1/completions',
             headers = {
                 'Content-Type': 'application/json',
                 'Authorization': f'Bearer {key}'
             },
             json = {
                 'model': 'text-davinci-003',
                 'prompt': f'{msg}',
                 'temperature': 0.4,
                 'max_tokens': 300
             }
         )
        json = response.json()
        #await ctx.send(response.status_code)
        await ctx.send(json['choices'][0]['text'])



    @commands.command()
    async def hello(self,ctx):
        await ctx.send(f"Hi <@{ctx.author.id}>")
        await ctx.send(ctx.author.name) #this is str

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