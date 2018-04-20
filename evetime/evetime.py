import discord
from discord.ext import commands
from time import gmtime,strftime

class EVETime:
    """A simple cog to output the current time in EVE Online"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def evetime(self):
        """A simple cog to output the current time in EVE Online"""
        
        #Your code will go here
        await self.bot.say(strftime("EVE time is currently **%H:%M:%S** on **%d/%m/%Y**", gmtime()))

def setup(bot):
    bot.add_cog(EVETime(bot))
