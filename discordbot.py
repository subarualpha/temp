from discord.ext import commands
from os import getenv
import traceback

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
