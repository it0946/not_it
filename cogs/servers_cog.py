from discord.ext import commands
from util.servers import add_server, server_exists
import json

class servers_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_guild_join')
    async def on_guild_join(self, ctx):
        if not  await server_exists(ctx.id):
            default_prefix = json.load(open('config.json', 'r'))['default_prefix']
            await add_server(ctx.id, ctx.name, default_prefix)

def setup(bot):
    bot.add_cog(servers_cog(bot))
