# Müzik komutları burada
import discord
from discord.ext import commands
import yt_dlp

import asyncio

# FFmpeg ayarları
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

YDL_OPTIONS = {'format': 'bestaudio'}

async def play_song(ctx, url):
    voice = ctx.voice_client

    if not voice:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
            voice = ctx.voice_client
        else:
            await ctx.send("You must be in a voice channel to use this command.")
            return

    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']
        source = await discord.FFmpegOpusAudio.from_probe(audio_url, **FFMPEG_OPTIONS)
        voice.play(source)
        await ctx.send(f"🎶 Now playing: **{info['title']}**")
