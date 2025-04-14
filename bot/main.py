import discord
from discord.ext import commands
import os

from bot import music  # music.py'yi içeri al

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot aktif: {bot.user}")

@bot.command(name="play")
async def play(ctx, url):
    await music.play_song(ctx, url)

@bot.command(name="stop")
async def stop(ctx):
    await music.stop_song(ctx)

bot.run(os.getenv("DISCORD_TOKEN"))
