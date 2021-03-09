from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionNotFound, ExtensionNotLoaded
import json

config = json.load(open('config.json', 'r'))
startup_extensions = ['test_cog', 'command_reaction', 'servers_cog']
bot = commands.Bot(command_prefix=commands.when_mentioned_or(config['default_prefix']))

async def isme(id: int): return(id == 273502808718704640)

cogs = { # Bool for if a cog is unloadable
    'main_cog': { 'startup': True, 'unloadable': False },
    'servers_cog': { 'startup': True, 'unloadable': False },
    'command_reaction': { 'startup': True, 'unloadable': True },
    'eon': { 'startup': False, 'unloadable': True }
}

for cog in cogs:
    if cogs[cog]['startup']:
        bot.load_extension('cogs.{0}'.format(cog))

# TODO: Implement a help command

@bot.group()
async def cog(ctx):
    if not await isme(ctx.author.id): return
    if ctx.invoked_subcommand is None:
        cogList = ""
        for cog in cogs:
            if cog[1]:
                cogList += '{0}\n'.format(cog)
        await ctx.send('Available cogs: ```{0}```'.format(cogList))

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot)) 

@cog.command()
async def unload(ctx, cog):
    try:
        if cogs[cog]['unloadable'] == True:
            print('{0.id} | {0}: unloaded {1}'.format(ctx.message.author, cog))
            bot.unload_extension('cogs.' + cog)
        else:
            await ctx.send('That cog cannot be unloaded')
    except ExtensionNotLoaded:
        await ctx.send('Error while unloading cog: Requested Cog is not loaded or found.')

@cog.command()
async def load(ctx, cog):
    try:
        print('{0.id} | {0}: loaded {1}'.format(ctx.message.author, cog))
        bot.load_extension('cogs.' + cog)
    except ExtensionAlreadyLoaded:
        bot.reload_extension('cogs.{0}'.format(cog))
        await ctx.send('`{0}` was already loaded so it was reloaded instead.'.format(cog))
    except ExtensionNotFound:
        await ctx.send('Error while loading cog: Requested Cog not found.')

@cog.command()
async def reload(ctx, ext):
    try:
        print('{0.id} | {0}: reloaded {1}'.format(ctx.message.author, ext))
        bot.reload_extension('cogs.{0}'.format(ext))
    except ExtensionNotFound:
        await ctx.send('Error while reloading cog: Requested Cog not found.')

bot.run(config['token'])
