import discord
from discord.ext import commands
from util.config import Config
from util.servers import Servers

config = Config
servers = Servers

async def get_prefix(bot, message: discord.Message):
    prefixes = [f'<@{bot.user.id}> ', f'<@!{bot.user.id}> ']
    if message.guild is None:
        prefix = await config.default_prefix
    else:
        prefix = await servers.

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

        super().__init__(
            intents=intents,
            command_prefix = get_prefix,
            description= 'Discord bot for learning and messing around'
            )

    async def process_commands(self, message):
        return super().process_commands(message)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send(f'')

    async def log(self):
        pass 

    async def run(self, *args, **kwargs):
        return super().run(*args, **kwargs)


    '''
    some sort of logging
    on_ready # No clue
    process_commands
    on_guild_join
    on_message
    run
    close
    spam_control
    '''
