import discord
from discord.ext import commands
import random

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='test', help='Responses with a random quote from B99')
    async def nine_nine(ctx):
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]
        response = random.choice(brooklyn_99_quotes)
        await ctx.send(response)
        
def setup(client):
    client.add_cog(Test(client))