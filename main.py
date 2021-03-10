from discord.ext import commands
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionNotFound, ExtensionNotLoaded
import json

from util.servers import add_server, server_exists, get_prefix

config = json.load(open('config.json', 'r'))

bot = commands.Bot(command_prefix=get_prefix)

async def isme(id: int): return(id == 273502808718704640)

# If startup is true, it will be loaded on startup. If unloadable is false it cannot be unloaded.
cogs = {  
    'main_cog': { 'startup': True, 'unloadable': False },
    'servers_cog': { 'startup': True, 'unloadable': False },
    'command_reaction': { 'startup': True, 'unloadable': True },
    'eon': { 'startup': False, 'unloadable': True }
}

for cog in cogs:
    if cogs[cog]['startup']:
        bot.load_extension('cogs.{0}'.format(cog))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}') 
    for guild in bot.guilds: # Add guilds which the bot joined while offline  
        if not await server_exists(guild.id):
            await add_server(guild.id, guild.name, config['default_prefix'])
            print(f'Added guild: {guild.name} to servers.json')

# TODO: Implement a help command

@bot.group()
async def cog(ctx):
    if not await isme(ctx.author.id): return
    if ctx.invoked_subcommand is None:
        cogList = ""
        for cog in cogs:
            if cog[1]:
                cogList += '{0}\n'.format(cog)
        await ctx.send(f'Available cogs: ```{cogList}```')


@cog.command()
async def unload(ctx, cog):
    try:
        if cogs[cog]['unloadable'] == True:
            print('{0.id} | {0}: unloaded {1}'.format(ctx.message.author, cog))
            bot.unload_extension('cogs.' + cog)
        else:
            await ctx.send('{0} cannot be unloaded'.format(cog))
    except ExtensionNotLoaded:
        await ctx.send(f'Error while unloading {cog}: Requested Cog is not loaded or found.')

@cog.command()
async def load(ctx, cog):
    try:
        print('{0.id} | {0}: loaded {1}'.format(ctx.message.author, cog))
        bot.load_extension('cogs.' + cog)
    except ExtensionAlreadyLoaded:
        bot.reload_extension('cogs.{0}'.format(cog))
        await ctx.send(f'`{cog}` was already loaded so it was reloaded instead.')
    except ExtensionNotFound:
        await ctx.send(f'Error while loading {cog}: Requested Cog not found.')

@cog.command()
async def reload(ctx, cog):
    try:
        print('{0.id} | {0}: reloaded {1}'.format(ctx.message.author, cog))
        bot.reload_extension('cogs.{0}'.format(cog))
    except ExtensionNotFound:
        await ctx.send('Error while reloading {0}: Requested Cog not found.'.format(cog))

bot.run(config['token'])
