from discord.ext import commands
from util.config import change_prefix
import json

config = json.load(open('config.json', 'r'))

class test_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx, prefix: str = None):
        if prefix is None:
            await ctx.send('The current prefix is: `{0}`'.format(config['prefix']))
        else:
            if not len(prefix) >= 4: 
                await change_prefix(prefix)
                self.bot.command_prefix = config['prefix'] = prefix
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