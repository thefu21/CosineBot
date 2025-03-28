import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

ytdlp_format_options = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'extract_flat': 'in_playlist'
}

FFMPEG_OPTIONS = {
    'options': '-vn'
}

@bot.event
async def on_ready():
    print(f'🎶 Bot online als {bot.user}!')

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("🔊 Joined the voice channel!")
    else:
        await ctx.send("❌ Du bist in keinem Voice-Channel!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Bot hat den Channel verlassen.")
    else:
        await ctx.send("❌ Bot ist in keinem Voice-Channel.")

@bot.command()
async def play(ctx, url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_url = None
        for fmt in info_dict.get('formats', []):
            if 'acodec' in fmt and fmt['acodec'] != 'none':
                audio_url = fmt['url']
                break

    if audio_url:
        if not ctx.voice_client:
            channel = ctx.author.voice.channel
            await channel.connect()

        voice_client = ctx.voice_client
        source = await discord.FFmpegOpusAudio.from_probe(audio_url)
        voice_client.play(source)
        await ctx.send(f"🎶 Now playing: {info_dict['title']}")
    else:
        await ctx.send("❌ Kein gültiger Audio-Stream gefunden.")

@bot.command()
async def stop(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("⏹ Wiedergabe gestoppt.")
    else:
        await ctx.send("❌ Es läuft nichts gerade.")

# Bot starten
bot.run(TOKEN)