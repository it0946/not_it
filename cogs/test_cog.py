from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

class test_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send('tesst')

    @commands.command()
    async def hellothere(self, ctx):
        await ctx.reply('General kenobi')

def setup(bot):
    bot.add_cog(test_cog(bot))