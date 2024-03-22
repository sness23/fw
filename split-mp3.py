from pydub import AudioSegment
from pydub.silence import split_on_silence

audio = AudioSegment.from_file("fw.mp3")

chunks = split_on_silence(audio,
    min_silence_len=600,  # Silence longer than 1000 ms (1 second)
    silence_thresh=-40    # Silence quieter than -40 dBFS
)

for i, chunk in enumerate(chunks):
    chunk.export(f"chunk{i}.mp3", format="mp3")
