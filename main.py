import discord
from discord.ext import commands
import youtube_dl
import os
from dotenv import load_dotenv
import json, requests, time
from datetime import date

load_dotenv()
token = os.environ.get("TOKEN")
yt_api_key = os.environ.get("YT_API_KEY")
yt_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC9OmOMZS6rU0_jIdZOxSHxw&maxResults=1&order=date&type=video&key=" + yt_api_key

intents = discord.Intents.default()
intents.members = True
last_played = ""

client = commands.Bot(command_prefix="!", intents=intents)

def get_latest_silksong():
    url = requests.get(yt_url)
    text = url.text
    data = json.loads(text)
    video_id = data["items"][0]["id"]["videoId"]
    ss_url = "https://youtu.be/" + video_id
    return ss_url

@client.event
async def on_voice_state_update(member, before, after):
    global last_played
    # current vc is none
    if after == None:
        return
    
    # check if ben
    if member.name != "parasol24":
        return
    
    #check if played
    today = date.today().strftime("%d/%m/%Y")
    if last_played == today:
        return

    url = get_latest_silksong()
    voiceChannel = after.channel
    song_there = os.path.isfile("song.mp3")
    
    if song_there:
        os.remove("song.mp3")
    
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    last_played = today 
    while voice.is_playing():
        time.sleep(1)
    
    await voice.disconnect()

client.run(token)
