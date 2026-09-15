import os

from pytubefix import YouTube
from pytubefix.cli import on_progress


def audio_only(urls, playlist_name):
    music_dir = os.path.join("music", playlist_name)
    os.makedirs(music_dir, exist_ok=True)

    for url in urls:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.get_audio_only()
        final_path = os.path.join(music_dir, stream.default_filename)

        if os.path.exists(final_path):
            print(f"Skip: {yt.title} -> {final_path} già presente")
            continue

        print(f"Scarico: {yt.title}")
        stream.download(output_path=music_dir)

playlists = [
    {
        "name" : "Eerie",
        "songs" :  [
            "https://www.youtube.com/watch?v=Wdas8OCA_l8",
            "https://www.youtube.com/watch?v=FWqlPktcq44",
            "https://www.youtube.com/watch?v=1mnthGkCabo",
            "https://www.youtube.com/watch?v=OZzgxCVBa1M",
            "https://www.youtube.com/watch?v=LoivAYusP_s",
            "https://www.youtube.com/watch?v=HeZP8tVGAUI",
            "https://www.youtube.com/watch?v=qEzWqUhnbVA",
            "https://www.youtube.com/watch?v=jUQmEiqBuqk",
            "https://www.youtube.com/watch?v=_9s5uvhhSJk",
            "https://www.youtube.com/watch?v=f717iNkYNLk",
            "https://www.youtube.com/watch?v=gP-vzhxSeqo"
        ]
    },
    {
        "name" : "Sad",
        "songs" : [
            "https://www.youtube.com/watch?v=hffMLTmRe9A",
            "https://www.youtube.com/watch?v=NJIhlzS5-jI",
            "https://www.youtube.com/watch?v=qEzWqUhnbVA",
            "https://www.youtube.com/watch?v=nXtY-NhSG7s",
            "https://www.youtube.com/watch?v=L8MsNJEfySY",
            "https://www.youtube.com/watch?v=qrG49Cpmqi8"
        ]
    },
    {
        "name" : "Epic/Fight",
        "songs" : [
            "https://www.youtube.com/watch?v=TSt_8MP1lLc",
            "https://www.youtube.com/watch?v=M1H8oswC9TY",
            "https://www.youtube.com/watch?v=7KnX-sM16iE",
        ]
    },
    {
        "name" : "Adventure/Chill",
        "songs" : [
            "https://www.youtube.com/watch?v=sR1OHW_IReI",
            "https://www.youtube.com/watch?v=YmSUajmPPPQ",
            "https://www.youtube.com/watch?v=MRp4i74bm_E",
            "https://www.youtube.com/watch?v=ErEGz0HHHOo",
            "https://www.youtube.com/watch?v=NV9MuoZtMUY",
            "https://www.youtube.com/watch?v=YBq-Bb833CY",
            "https://www.youtube.com/watch?v=jw457e-KKkA",
            "https://www.youtube.com/watch?v=8i4RVdu9KH0",
            "https://www.youtube.com/watch?v=2Q10drmGOaA"
        ]
    },
    {
        "name" : "Bitter happiness/Farewell",
        "songs" : [
            "https://www.youtube.com/watch?v=E7qKVWGn4j4",
            "https://www.youtube.com/watch?v=6dgmy3JXz3g",
            "https://www.youtube.com/watch?v=1GCoO6f7cE4"
        ]
    },
    {
        "name" : "Adventure/Epic",
        "songs" : [
            "https://www.youtube.com/watch?v=XvymAXxAa60",
            "https://www.youtube.com/watch?v=NQlYkuFycrw"
        ]
    }
]

for playlist in playlists:
    name = playlist['name']
    songs = playlist.get('songs', [])
    if songs:
        audio_only(songs, name)