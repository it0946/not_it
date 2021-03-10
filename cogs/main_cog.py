from logging import NullHandler
from discord.ext import commands
from util.servers import change_prefix, get_guild_prefix, get_prefix
import json

class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Figure out how to properly do permissions for commands
    @commands.command()
    async def prefix(self, ctx, prefix: str = None):
        server_config = json.load(open('servers.json', 'r'))
        _prefix = await get_guild_prefix(ctx.guild.id)
        if prefix is None:
            await ctx.send(f'The current prefix is: `{prefix}`, or you can ping the bot.')
        else:
            if not len(prefix) > 4:
                if prefix == _prefix:
                     await ctx.send('New prefix cannot be the old prefix.')
                     return
                await change_prefix(ctx.guild.id, prefix)
                await ctx.send(f'Success: The new bot prefix is `{prefix}`')
            else: 
                await ctx.send('Requested prefix is too long. Limit is 4 characters')

    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send('tesst')

    @commands.command()
    async def hellothere(self, ctx):
        await ctx.reply('General kenobi')

def setup(bot):
    bot.add_cog(main_cog(bot))
