import discord
from discord.ext import commands
from core.classes import Cog_extension
import pymysql

class Note(Cog_extension):
    def __init__(self,bot):
        self.bot = bot
    

    


      
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