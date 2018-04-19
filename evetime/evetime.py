import discord
from discord.ext import commands
from time import gmtime,strftime

class EVETime:
    """A simple cog to output the current EVE time"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def evetime(self):
        """A simple cog to output the current EVE time"""

        #Your code will go here
        await self.bot.say(strftime("The current EVE time is **%d/%m/%Y - %H:%M:%S**", gmtime()))

def setup(bot):
    bot.add_cog(EVETime(bot))
