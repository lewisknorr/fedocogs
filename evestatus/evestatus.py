import discord
from discord.ext import commands
import pyping

class evestatus:
    """Check the server status of Tranquility"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tq(self):
        """This does stuff!"""

        #Your code will go here
        r = pyping.ping("https://esi.tech.ccp.is/latest/status/?datasource=tranquility")

        if r.ret_code == 0:
            print("Tranquility is online")
        else:
            print("Tranquility is offline")


def setup(bot):
    bot.add_cog(tq(bot))
