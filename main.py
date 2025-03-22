import os
import discord
from dotenv import load_dotenv
from lib.fivesim import FiveSim
from discord.ext import commands

load_dotenv() 
bot = commands.Bot(command_prefix="-", self_bot=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.reply(f"Pong!\nLatency: {round(bot.latency * 1000, 2)}", delete_after=5)

@bot.command()
async def fivesim(ctx, type=None, product=None, country=None):
    if (type, product, country) == (None, None, None):
        await ctx.reply("```[Help]```")
    fivesim = FiveSim()
    match type:
        case "balance":
            balance = fivesim.get_balance()
            await ctx.reply(f"{balance}RUB")
        case _:
            await ctx.reply("wrong args.\nrun -fivesim for help")
            


bot.run(os.getenv("TOKEN"))