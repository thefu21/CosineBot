import yt_dlp

# URL des YouTube-Videos oder -Streams
youtube_url = "https://www.youtube.com/watch?v=Uw5OLnN7UvM"

# yt-dlp Optionen
ydl_opts = {
    'format': 'bestaudio/best',  # Wähle die beste Audioqualität
    'noplaylist': True,           # Spielt nur das angegebene Video ab, nicht die gesamte Playlist
    'quiet': True,                # Unterdrückt Statusmeldungen
}

# Informationen abrufen
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)  # download=False für kein Download
    audio_url = None

    # Suche nach der besten Audio-URL
    for fmt in info_dict.get('formats', []):  # Verwende get(), um einen leeren Array zurückzugeben, falls 'formats' nicht existiert
        if 'acodec' in fmt and fmt['acodec'] != 'none':  # Überprüfen, ob 'acodec' vorhanden ist
            audio_url = fmt['url']
            break  # Beende die Schleife nach dem ersten Treffer

    if audio_url:
        print(f"Audio-Stream-URL: {audio_url}")  # Gib die Audio-Stream-URL aus
    else:
        print("Keine gültige Audio-Stream-URL gefunden.")
