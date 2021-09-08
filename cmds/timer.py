from discord.ext import commands
from threading import Timer

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.end = 0
        self.breakmode = 0
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Bot is online.')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')
        
    @commands.command()
    async def stop(self, ctx): #stops the cycle
        await ctx.send('Congrats, we done')
        self.end = 1

    @commands.command(help='Sets Pomodoro timer | Usage: .set [focus time] [short break] [long break]')
    async def set(self, ctx, arg1, arg2, arg3):
        await ctx.send('You passed {} and {} and {}'.format(arg1, arg2, arg3))
        print('Started')
        
        #initializing
        self.end = 0
        self.breakmode=0
        
        # convert arguments from strings to integers
        try:
            focus = int(arg1)
            short = int(arg2)
            long = int(arg3)
        except:
            await ctx.send('Oops! Looks like you didn\'t enter an integer value for time!')
            return
        # check that it is not already running
        
        # start focus time
            # render timer
        await self.focusMode(ctx, focus, short, long)
        # set timer
        # tags user and sends message

    async def focusMode(self, ctx, focus, short, long):
        await ctx.send('Focussing')
        #initializing
        focusToShort = Timer(focus*60, self.shortMode, (focus, short, long))
        focusToLong = Timer(focus*60, self.longMode, (focus, short, long))
        
        # if we want out
        if self.end == 1:
            return
        
        if self.breakmode == 3: #long break
            focusToLong.start()
            self.breakmode = 0
        else: # short break
            focusToShort.start()
            self.breakmode= self.breakmode + 1 
        
        #loop 
        #sends time to focus message
        # triggers focus duration
        # duration triggers short break
        return
    
    async def shortMode (self, ctx, focus, short, long):
        if self.end == 1:
            return
        
        await ctx.send('Short break')
        shortToFocus = Timer(short*60, self.focusMode, (focus, short, long))
        shortToFocus.start()
        return
    
    async def longMode (self, ctx, focus, short, long):
        if self.end == 1:
            return
        
        await ctx.send('Long break')
        longToFocus = Timer(long*60, self.focusMode, (focus, short, long))
        longToFocus.start()
        # set timer
        return
    
    def displayTimer(self, ctx, time):
        pass

def setup(client):
    client.add_cog(Example(client))
