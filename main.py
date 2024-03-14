import moviepy.editor

from yt_dlp import YoutubeDL

# video = 'https://vk.com/video-149258223_456242929'
# video = 'https://www.youtube.com/watch?v=5aYwU4nj5QA'
video = input("Ссылка на видео: ")
youtube_dl_opts = {}

with YoutubeDL(youtube_dl_opts) as ydl:
    ydl.download(video)

    info_dict = ydl.extract_info(video, download=False)
    video_url = info_dict.get("url", None)
    video_id = info_dict.get("id", None)
    video_title = info_dict.get('title', None)

input1 = input('\n\n1. Извлечь звук\n-  ')

if input1 == '1':
    video = moviepy.editor.VideoFileClip(f"{video_title} [{video_id}].mp4")
    audio = video.audio
    audio.write_audiofile(f"{video_title} [{video_id}].mp3")
    print("Звук извлечен")
input()
