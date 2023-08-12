import discord
from discord.ext import commands
from core.classes import Cog_extension
import pymysql

class Note(Cog_extension):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def show_sql(self,ctx):
        await ctx.channel.send("link success")

        # 修改为你的数据库连接信息
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "0811_py"
        }

        try:
            connection = pymysql.connect(**db_config)
            print("Successfully connected to the database.")

            cursor = connection.cursor()

            query = "SELECT * FROM my_note"
            cursor.execute(query)
            print("Query executed successfully.")

            results = cursor.fetchall()

            for row in results:
                await ctx.channel.send(row)

        except pymysql.MySQLError as e:
            print("Error:", e)


    @commands.command()
    async def add_note(self,ctx,name,month,day):
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "0811_py"
        }
        try:
            insert_query = f"INSERT INTO my_note (name, month, day) VALUES (%s, %s, %s)"
            values = (name, int(month), int(day))
            connection = pymysql.connect(**db_config)
            print("Successfully connected to the database.")

            cursor = connection.cursor()
            cursor.execute(insert_query, values)

            connection.commit()
            await ctx.channel.send("Data inserted successfully.")
        except pymysql.MySQLError as e:
    # 处理错误
            print("Error:", e)
            connection.rollback()


    @commands.command()
    async def delete_note(self, ctx, id):
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "0811_py"
        }
        try:
            delete_query = "DELETE FROM my_note WHERE id = %s"
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