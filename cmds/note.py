import discord
from discord.ext import commands
from core.classes import Cog_extension
import pymysql

class Note(Cog_extension):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def link_sql(self,ctx,msg):
        await ctx.channel.send("link success")

        # 修改为你的数据库连接信息
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "0419test"
        }

        try:
            connection = pymysql.connect(**db_config)
            print("Successfully connected to the database.")

            cursor = connection.cursor()

            query = "SELECT * FROM customers"
            cursor.execute(query)
            print("Query executed successfully.")

            results = cursor.fetchall()

            for row in results:
                await ctx.channel.send(row)

        except pymysql.MySQLError as e:
            print("Error:", e)

#query = "SELECT * FROM your_table"
#cursor.execute(query)
#print("Query executed successfully.")
#
#results = cursor.fetchall()
#
#for row in results:
#    print(row)

async def setup(bot):
    await bot.add_cog(Note(bot))