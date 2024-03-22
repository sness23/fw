import librosa
import numpy as np
import soundfile as sf

def find_silent_sections(audio, sr, threshold=0.02, frame_length=2048, hop_length=512):
    """
    Find silent sections in an audio signal.
    
    :param audio: Audio time series
    :param sr: Sampling rate of `audio`
    :param threshold: Amplitude threshold to consider a frame silent
    :param frame_length: Length of each frame for analysis
    :param hop_length: Number of samples to hop between frames
    :return: List of start and end frames of silent sections
    """
    # Compute the short-time energy
    energy = np.array([sum(abs(audio[i:i+frame_length]**2))
                       for i in range(0, len(audio), hop_length)])
    
    # Normalize energy
    max_energy = np.max(energy)
    energy = energy / max_energy
    
    # Find frames below the threshold
    silent_frames = np.where(energy < threshold)[0]
    
    # Group silent frames into continuous sections
    silent_sections = []
    if len(silent_frames):
        start_frame = silent_frames[0]
        for i in range(1, len(silent_frames)):
            if silent_frames[i] > silent_frames[i-1] + 1:
                end_frame = silent_frames[i-1]
                silent_sections.append((start_frame, end_frame))
                start_frame = silent_frames[i]
        silent_sections.append((start_frame, silent_frames[-1]))
    
    # Convert frame numbers to time
    silent_sections_time = [(start * hop_length / sr, end * hop_length / sr) for start, end in silent_sections]
    
    return silent_sections_time

# Load audio file
audio, sr = librosa.load("fw0.wav", sr=None)

# Find silent sections
silent_sections = find_silent_sections(audio, sr)

# Split and save audio based on silent sections (this is a simple approach and might need refinement)
for i, section in enumerate(silent_sections[:-1]):
    start_sample = int(section[1] * sr)
    end_sample = int(silent_sections[i + 1][0] * sr)
    chunk = audio[start_sample:end_sample]
    sf.write(f'chunk_{i}.wav', chunk, sr)

