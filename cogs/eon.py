from discord.ext import commands
from util.config import delid, addid, id_exists
import random

class eon(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot    

    @commands.Cog.listener('on_message')
    async def on_message(self, ctx):
        eon_replies = ['hi eon', 'hey eon', 'hello there eon', 'hej eon', 'AAAAAAAAAAAAAAAA']
        if await id_exists(ctx.author.id):
            if ctx.author.id == 137586984347631616:
                await ctx.reply(random.choice(eon_replies))
            else:
                reply = random.choice(eon_replies)
                await ctx.reply(reply.replace('eon', 'not eon'))
        else: 
            return

    @commands.command()
    async def eon(self, ctx):
        await ctx.send('Eon')

    @commands.command()
    async def addperson(self, ctx, id: int = None):
        if id is None:
            await addid(ctx.author.id)
        else:
            await addid(id)

    @commands.command()
    async def delperson(self, ctx, id: int = None):
        if id is None:
            await delid(ctx.author.id)
        else:
            await delid(id) 

def setup(bot):
    bot.add_cog(eon(bot))