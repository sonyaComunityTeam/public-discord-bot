import discord
import load_env
import aiohttp
import pyshortners
import asyncio

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="そにゃコミュニティPublic Bot"))

@bot.slash_command(guild_ids=[1006776654934323260], name="URL", description="URLを圧縮・展開します。")
async def expandurl(
    ctx,
    typ: Option(str, '', choices=['短縮', '展開']),
    link: Option(str, '短縮・展開をするURLを入力')
):
    if typ == "展開":
        async with aiohttp.ClientSession() as session:
            expand = session.get(link).url
            await ctx.respond(f"URLを展開しました。:{expand}")
    elif typ == "短縮":
            await ctx.respond(f"URLを短縮しました。:{tyny}")

bot.run(load_env.DISCORD_TOKEN)
