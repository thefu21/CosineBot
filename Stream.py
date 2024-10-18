import streamlink
import subprocess

# URL des Streams
stream_url = "DEIN_STREAM_LINK"

# Abrufen der verfügbaren Streams
streams = streamlink.streams(stream_url)

# Wähle die beste Qualität (du kannst auch explizit eine andere Qualität angeben, z.B. "audio_only")
best_stream = streams['best']

# Verwende ffplay, um den Audio-Stream direkt abzuspielen (ffmpeg muss installiert sein)
command = [
    "ffplay",
    "-vn",  # Deaktiviert Video (nur Audio)
    best_stream.url  # URL des Audio-Streams
]

# Starte das Abspielen
subprocess.run(command)