import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import getStats  # Import the getStats module, assuming it's properly set up

load_dotenv()
TOKEN = os.getenv('TOKEN')

# Create an instance of a client with intents
intents = discord.Intents.all()
intents.message_content = True  # Enable the message content intent
intents.guilds = True           # Enable the guilds intent (for server events)

# Create a bot instance with specified intents
bot = commands.Bot(command_prefix='>', intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to respond to ">hello"
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

# Command to get user stats
@bot.command(name='gs', help='Fetches osu! stats for the given username.\nUsage: `>gs <osu_username>`\nExample: `>gs Bernso`')
async def get_stats(ctx, username):
    try:
        # Directly await the coroutine from getStats
        stats = await getStats.main(username)
        await ctx.reply(stats)
    except Exception as e:
        await ctx.reply(f"An error occurred: {e}")


# Run the bot with your token
bot.run(TOKEN)
