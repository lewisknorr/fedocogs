import discord
from discord.ext import commands
import pyping

class FedoCogs:
    """Check the server status of Tranqulity"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tq(self):
        """Is Tranquility online?"""

        #Your code will go here
        r = pyping.ping("https://esi.tech.ccp.is/latest/status/?datasource=tranquility")

        if r.ret_code == 0:
            await self.bot.say("Tranquility is online!")
        else:
            await self.bot.say("Tranquility is offline")

def setup(bot):
    bot.add_cog(FedoCogs(bot))
