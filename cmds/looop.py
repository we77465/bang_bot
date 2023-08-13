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

    def cog_unload(self):          #取消loop
        self.printer.cancel()

    @commands.command()            #設定channel要輸出的頻道
    async def set_channel(self, ctx, msg: int):
        self.channel = self.bot.get_channel(msg)
        await ctx.send(f"change to {self.channel.mention}")



    @tasks.loop(seconds=1.0)  # 每一秒執行 如果在分%5==0的時候 send東西 
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


















    def is_valid_date(self,year, month, day):
        if month < 1 or month > 12:
            return False
    
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return day <= 29
            else:
                return day <= 28
        elif month in [4, 6, 9, 11]:
            return day <= 30
        else:
            return day <= 31  


    @commands.command()
    async def show_note(self,ctx):
        await ctx.channel.send("link success")

        # 修改为你的数据库连接信息
        db_config = {
            "host": "localhost",
            "user": jdata["user"],
            "password": "",
            "database": jdata["database"]
        }

        try:
            connection = pymysql.connect(**db_config)
            print("Successfully connected to the database.")

            cursor = connection.cursor()

            query = "SELECT * FROM my_note2"
            cursor.execute(query)
            print("Query executed successfully.")

            results = cursor.fetchall()

            for row in results:
                await ctx.channel.send(row)

        except pymysql.MySQLError as e:
            print("Error:", e)


    @commands.command()
    async def add_note(self,ctx,year:int,month:int,day:int):
        name = ctx.author.name
        db_config = {
            "host": "localhost",
            "user": jdata["user"],
            "password": "",
            "database": jdata["database"]
        }
        #await ctx.channel.send(self.is_valid_date(year, month, day))
        if self.is_valid_date(year, month, day):
            try:
                insert_query = f"INSERT INTO my_note2 (name, year ,month, day) VALUES (%s, %s, %s, %s)"
                values = (name,int(year) ,int(month), int(day))
                connection = pymysql.connect(**db_config)
                print("Successfully connected to the database.")

                cursor = connection.cursor()
                cursor.execute(insert_query, values)

                connection.commit()
                print(ctx.channel)
                await ctx.channel.send("Data inserted successfully.")
                print("123")
            except pymysql.MySQLError as e:
        # 处理错误
                print("Error:", e)
                connection.rollback()
        else:
            await ctx.channel.send("無效的日期")

    

    @commands.command()
    async def delete_note(self, ctx, id):
        db_config = {
            "host": "localhost",
            "user": jdata["user"],
            "password": "",
            "database": jdata["database"]
        }
        try:
            delete_query = "DELETE FROM my_note2 WHERE id = %s"
            values = (id,)

            connection = pymysql.connect(**db_config)
            print("Successfully connected to the database.")

            cursor = connection.cursor()
            cursor.execute(delete_query, values)

            connection.commit()
            await ctx.channel.send("Data deleted successfully.")
        except pymysql.MySQLError as e:
            # 处理错误
            print("Error:", e)
            connection.rollback()
        finally:
            connection.close()


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

