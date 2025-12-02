from yt_dlp import YoutubeDL

url = "https://youtu.be/lYO4tppyEE0?si=6gSBbI9OXXjkkIab"

ydl_opts = {
    "format": "mp4/best",
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])