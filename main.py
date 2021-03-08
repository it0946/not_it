from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionNotFound, ExtensionNotLoaded
import json

config = json.load(open('config.json', 'r'))
startup_extensions = ['test_cog', 'command_reaction']
bot = commands.Bot(command_prefix=commands.when_mentioned_or(config['prefix']))

async def isme(id: int): return(id == 273502808718704640)

for e in startup_extensions:
    bot.load_extension('cogs.{0}'.format(e))

@bot.group()
async def cog(ctx):
    if not await isme(ctx.author.id): return
    if ctx.invoked_subcommand is None:
        _cogs = ""
        for item in startup_extensions: _cogs += '{0} '.format(item)
        await ctx.reply('Available cogs: ```{0}```'.format(_cogs))

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot)) 

@cog.command()
async def unload(ctx, ext):
    try:
        print('{0.id} | {0}: unloaded {1}'.format(ctx.message.author, ext))
        bot.unload_extension('cogs.' + ext)
    except ExtensionNotLoaded:
        await ctx.reply('Error while unloading cog: Requested Cog is not loaded or found.')

@cog.command()
async def load(ctx, ext):
    try:
        print('{0.id} | {0}: loaded {1}'.format(ctx.message.author, ext))
        bot.load_extension('cogs.' + ext)
    except ExtensionAlreadyLoaded:
        await ctx.reply('Error while loading cog: Cog is already loaded.')
    except ExtensionNotFound:
        await ctx.reply('Error while loading cog: Requested Cog not found.')

@cog.command()
async def reload(ctx, ext):
    try:
        print('{0.id} | {0}: reloaded {1}'.format(ctx.message.author, ext))
        bot.reload_extension('cogs.{0}'.format(ext))
    except ExtensionNotFound:
        await ctx.reply('Error while reloading cog: Requested Cog not found.')

bot.run(config['token'])
