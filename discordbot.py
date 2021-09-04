from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

reply_data = {}
@bot.command()
async def ori(ctx, word, reply):
    reply_data[word] = reply
    await ctx.send(f"{word} -> {reply}を登録しました")

@bot.event
async def on_message(message):
    reply = reply_data.get(message.content)
    if reply:
        await message.channel.send(reply)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
