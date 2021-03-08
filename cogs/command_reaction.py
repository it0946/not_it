from discord.ext import commands

class command_reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener('on_command')
    async def on_command(self, ctx):
        if not ctx.command_failed:
            print('{0.guild}: {0.channel} | {0.author.id} {0.author}: Executed {0.command}'.format(ctx))
            await ctx.message.add_reaction('✅')
        
    
    #@commands.Cog.listener('on_command_error')
    #async def on_command_error(self, ctx):
    #    await ctx.message.add_reaction('❌')

def setup(bot):
    bot.add_cog(command_reaction(bot))