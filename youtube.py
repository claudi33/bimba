from yt_dlp import YoutubeDL

url = "https://youtu.be/_Xa_v7eD2Eg?si=uh-HXo5gki1kgk9v"

ydl_opts = {
    "format": "mp4/best",
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])