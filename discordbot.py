from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='help.')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = 'エラーメッセージ'
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command(name="久しぶり")
async def hello(ctx):
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
