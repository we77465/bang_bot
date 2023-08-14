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
        self.db_config = {
            "host": jdata["host"],
            "user": jdata["user"],
            "password": "",
            "database": jdata["database"]
        }
        self.connection = pymysql.connect(**self.db_config)
        self.currentuser = "worstking99"
        self.five_min = -1


    @commands.command()
    async def unloop(self,ctx):          #取消loop
        self.printer.cancel()
        await ctx.channel.send("cancel success")

    @commands.command()
    async def loop(self,ctx):          #loop
        self.printer.start()
        await ctx.channel.send("loop success")

    @commands.command()            #設定channel要輸出的頻道
    async def set_channel(self, ctx, msg: int):
        self.channel = self.bot.get_channel(msg)
        await ctx.send(f"change to {self.channel.mention}")



    @tasks.loop(seconds=1.0)  # 每一秒執行 如果在分%5==0的時候 send東西 
    async def printer(self):
        now = datetime.datetime.now()
        if now.minute % 5 == 6 or now.second == 0:  # At exact 5th, 10th, 15th, ... minute
            
            if self.index == 0:
                await self.send_message()
            await self.channel.send(f"現在時間{now.hour}點{now.minute}分{now.second}秒")
            self.index += 1

            with self.connection.cursor() as cursor:
                # 執行查詢，擷取名為 "worstking99" 的記錄
                sql = "SELECT * FROM my_note2 WHERE name = %s ORDER BY year ASC, month ASC, day ASC,hours ASC,mins ASC"
                cursor.execute(sql, (f'{self.currentuser}',))

                # 取得所有符合條件的記錄
                records = cursor.fetchall()

                # 輸出擷取的記錄
                for record in records:
                    hours = int(record[5])
                    mins = int(record[6])
                    self.five_min = hours*60+mins
                    #await self.channel.send(self.five_min - (now.hour*60+now.minute))
                    if self.five_min - (now.hour*60+now.minute) ==5  :
                        await self.channel.send(record)
                        await self.channel.send("這個的時間再5分鐘就要到了哦")
                        self.five_min = -1

            

    async def send_message(self):
        self.channel = self.bot.get_channel(int(jdata["WELCOME"]))

    
    @commands.command()
    async def change_user(self,ctx):
        self.currentuser(ctx.author.name)
        await ctx.channel.send("change success")
    


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

        

        try:
            connection = pymysql.connect(**self.db_config)
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
        #db_config = {
        #    "host": jdata["host"],
        #    "user": jdata["user"],
        #    "password": "",
        #    "database": jdata["database"]
        #}
        #await ctx.channel.send(self.is_valid_date(year, month, day))
        if self.is_valid_date(year, month, day):
            try:
                insert_query = f"INSERT INTO my_note2 (name, year ,month, day) VALUES (%s, %s, %s, %s)"
                values = (name,int(year) ,int(month), int(day))
                connection = pymysql.connect(**self.db_config)
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
#@commands.command()
#    async def add_note(self,ctx,year:int,month:int,day:int,hours:int,mins:int):
#        name = ctx.author.name
#        #db_config = {
#        #    "host": jdata["host"],
#        #    "user": jdata["user"],
#        #    "password": "",
#        #    "database": jdata["database"]
#        #}
#        #await ctx.channel.send(self.is_valid_date(year, month, day))
#        if self.is_valid_date(year, month, day):
#            try:
#                insert_query = f"INSERT INTO my_note2 (name, year ,month, day,hours,mins) VALUES (%s, %s, %s, %s,%s ,%s)"
#                values = (name,int(year) ,int(month), int(day),int(hours,int(mins)))
#                connection = pymysql.connect(**self.db_config)
#                print("Successfully connected to the database.")
#
#                cursor = connection.cursor()
#                cursor.execute(insert_query, values)
#
#                connection.commit()
#                print(ctx.channel)
#                await ctx.channel.send("Data inserted successfully.")
#                print("123")
#            except pymysql.MySQLError as e:
#        # 处理错误
#                print("Error:", e)
#                connection.rollback()
#        else:
#            await ctx.channel.send("無效的日期")
    

    @commands.command()
    async def delete_note(self, ctx, id):
        #db_config = {
        #    "host": jdata["host"],
        #    "user": jdata["user"],
        #    "password": "",
        #    "database": jdata["database"]
        #}
        try:
            delete_query = "DELETE FROM my_note2 WHERE id = %s"
            values = (id,)

            connection = pymysql.connect(**self.db_config)
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

