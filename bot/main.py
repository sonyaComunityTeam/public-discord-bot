import discord
import load_env
import aiohttp
import asyncio

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="そにゃコミュニティPublic Bot"))

@bot.slash_command(guild_ids=[1006776654934323260], name="expandurl", description="Expand your TinyURL")
async def expandurl(ctx, url: str):
    if type == "展開":
        async with aiohttp.ClientSession() as session:
            expand = session.get(Link).url
            await ctx.respond(f"URLを展開しました。:{expand}")
    elif type == "短縮":
            await ctx.respond(f"URLを短縮しました。:{tyny}")

bot.run(load_env.DISCORD_TOKEN)
