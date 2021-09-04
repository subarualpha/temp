from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='s.')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = 'その質問に対してはまだ未実装です。\n運営又はサポートに問い合わせしてください'
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command(name="help.DDoS")
async def hello(ctx):
    await ctx.send(f"DDoS対策はTCPShieldを介してのIPv4接続となります。\nDDoS攻撃を受けた場合はそちらが対応してくれるので大丈夫ですが、\n万が一DDoSが直接来た場合、参加型を一時中断いたします")


@bot.command(name="help.サーバーに接続できない")
async def hello(ctx):
    await ctx.send(f"考えられる候補\n1.サーバーアドレスがあっているか、 #お知らせ を常時確認してください。\n2.サーバーが起動しているか、@Minecraft#5528 がオンラインになっているか確認してください。又はメンテナンスになっていないか確認してください\n3.サーバーのバージョンがあっていない。サーバーバージョンは1.17.1となっております(2021/9/5現在)\n4.非正規のランチャーを使っていないか、TLauncherなどの非正規クライアントの場合、サーバーに入ることはできませんのでご了承ください\nその他ご不明な点があればサポートからお問い合わせください")


@bot.command(name="help.TLauncher")
async def hello(ctx):
    await ctx.send(f"TLauncherは対応しておりません。ご了承ください")


@bot.command(name="help.badlion")
async def hello(ctx):
    await ctx.send(f"badlionは検証しておりませんが、一応参加はできると思います。ご不明な点がございましたらサポートへお問い合わせください")


@bot.command(name="help.チート")
async def hello(ctx):
    await ctx.send(f"チートクライアントの使用は一切許されておりません。発見次第BANいたします。")


@bot.command(name="help.サーバー")
async def hello(ctx):
    await ctx.send(f"サーバー情報\nSpigot1.17.1\n...")


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
