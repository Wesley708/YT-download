import yt_dlp

url = "https://youtu.be/zcvqYS6WeTQ"  # substitua pelo seu link

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',  # salva o arquivo com o título do vídeo
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
