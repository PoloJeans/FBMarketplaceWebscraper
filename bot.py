import discord
from discord.ext import commands
import subprocess

# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

@bot.command()
async def runfb(ctx):
    try:
        print("Command triggered")
        await ctx.send("Starting...")
        #Runs FB.py using subprocess
        result = subprocess.run(
            ["python3", "FB.py"],
            capture_output=True,
            text=True
        )
        output = result.stdout or result.stderr

        #If its good print
        if output:
            await ctx.send(f"Output:\n```\n{output[:1900]}\n```")
        else:
            await ctx.send(f"Error: {str(e)}")

    #Catches errors
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Replace 'YOUR_TOKEN_HERE' with your bot's token
bot.run("YOUR_TOKEN_HERE")
