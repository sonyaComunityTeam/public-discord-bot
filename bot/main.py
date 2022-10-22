import discord
import load_env

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="そにゃコミュニティPublic Bot"))

bot.run(load_env.DISCORD_TOKEN)
