import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

# when bot connects to discord servers
@bot.event  # event listener
async def on_ready():
    server_count = 0
    for server in bot.guilds:
        #print server names and ids
        print(f"- {server.id} (name: {server.name})")
        server_count = server_count + 1
    print("PomoBot is in " + str(server_count) + " servers.")

# for the commands in the cmds directory
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    
@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    bot.load_extension(f'cmds.{extension}')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

bot.run(TOKEN)
