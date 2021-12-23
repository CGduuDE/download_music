import pyglet
import youtube_dl

url = "https://www.youtube.com/watch?v=6aTYceNFDP4"

def download(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        ydl.download([url])

    return ydl.prepare_filename(info_dict)

def play_sound(name):
    song = pyglet.media.load(name)
    song.play()
    pyglet.app.run()

try:
    play_sound(download(url))
except:
    pass
