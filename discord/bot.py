import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import getStats  

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
intents.message_content = True  
intents.guilds = True           

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    """
    This event is triggered when the bot has successfully logged in and is ready to start receiving and processing events.

    Parameters:
    None

    Returns:
    None

    The function prints a message to the console indicating the bot's username.
    """
    print(f'Logged in as {bot.user.name}')

@bot.command(name='hello')
async def hello(ctx):
    """
    This function sends a greeting message to the Discord channel where the command was invoked.

    Parameters:
    ctx (discord.ext.commands.Context): The context object representing the invocation context.
        This object provides access to various properties and methods related to the event.

    Returns:
    None

    The function sends a message to the Discord channel using the `ctx.send()` method,
    including a greeting message along with the name of the author who invoked the command.
    """
    await ctx.send(f'Hello, {ctx.author.name}!')

@bot.command(name='gs', help='Fetches osu! stats for the given username.\nUsage: `>gs <osu_username>`\nExample: `>gs Bernso`')
async def get_stats(ctx, username):
    """
    Fetches and sends osu! stats for the given username to the Discord channel.

    Parameters:
    ctx (discord.ext.commands.Context): The context object representing the invocation context.
        This object provides access to various properties and methods related to the event.
    username (str): The osu! username for which to fetch the stats.

    Returns:
    None

    This function attempts to fetch the osu! stats for the given username using the `getStats.main()` function.
    If successful, it sends the stats to the Discord channel using the `ctx.reply()` method.
    If an error occurs during the fetching process, it sends an error message to the Discord channel.
    """
    try:
        stats = await getStats.main(username)
        await ctx.reply(stats)
    except Exception as e:
        await ctx.reply(f"An error occurred: {e}")


bot.run(TOKEN)
