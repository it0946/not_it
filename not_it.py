from os import pread
from sys import prefix
from discord.ext import commands
from discord.flags import Intents
import discord
import json

from util.servers import get_prefix

# WIP

class not_it(commands.Bot):
    def __init__(self):
        intents = discord.Intents(
            guilds = True,
            members = True,
            bans = True,
            emojis = True,
            messages = True,
            reactions = True
        )

        super().__init__(command_prefix=prefix, intents=intents)
        
    
