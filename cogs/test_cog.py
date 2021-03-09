from discord.ext import commands
from util.config import change_prefix
import json

class test_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Figure out how to properly do permissions for commands
    @commands.command()
    async def prefix(self, ctx, prefix: str = None):
        config = json.load(open('config.json', ))
        if prefix is None:
            await ctx.send('The current prefix is: `{0}`, or you can ping the bot.'.format(config['prefix']))
        else:
            if not len(prefix) > 4:
                if prefix == config['prefix']:
                     await ctx.send('New prefix cannot be the old prefix.')
                     return
                await change_prefix(prefix)
                self.bot.command_prefix = commands.when_mentioned_or(prefix)
                await ctx.send('Success: The new bot prefix is `{0}`'.format(prefix))
            else: 
                await ctx.send('Requested prefix is too long. Limit is 4 characters')

    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send('tesst')

    @commands.command()
    async def hellothere(self, ctx):
        await ctx.reply('General kenobi')

def setup(bot):
    bot.add_cog(test_cog(bot))