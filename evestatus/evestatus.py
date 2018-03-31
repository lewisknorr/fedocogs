import discord
from discord.ext import commands
import beautifulsoup4

...

try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False

...
