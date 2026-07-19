# import librosa
# import numpy as np
# from scipy.signal import find_peaks


# def analyze_audio(audio_path):

#     y, sr = librosa.load(audio_path, sr=None)

#     rms = librosa.feature.rms(y=y)[0]

#     times = librosa.frames_to_time(
#         np.arange(len(rms)),
#         sr=sr
#     )

#     # Detect peaks
#     peaks, _ = find_peaks(
#         rms,
#         prominence=np.max(rms) * 0.40,   # adjust later
#         distance=300                      # prevents nearby duplicate peaks
#     )

#     peak_values = rms[peaks]

#     sorted_indices = np.argsort(peak_values)[::-1]

#     peaks = peaks[sorted_indices[:10]]

#     peaks = np.sort(peaks)

#     return times, rms, peaks




import librosa
import numpy as np
from scipy.signal import find_peaks


def analyze_audio(audio_path):
    """
    Analyze crowd excitement from match audio.
    Returns:
        times  -> timestamps (seconds)
        rms    -> smoothed audio energy
        peaks  -> indices of detected exciting moments
    """

    # Load audio
    y, sr = librosa.load(audio_path, sr=None)

    # Compute RMS energy
    rms = librosa.feature.rms(y=y)[0]

    # Smooth the RMS signal
    window_size = 10
    rms = np.convolve(
        rms,
        np.ones(window_size) / window_size,
        mode="same"
    )

    # Convert frame indices to seconds
    times = librosa.frames_to_time(
        np.arange(len(rms)),
        sr=sr
    )

    # Adaptive threshold
    mean_energy = np.mean(rms)
    std_energy = np.std(rms)

    threshold = mean_energy + (1.2 * std_energy)

    # Detect peaks
    peaks, properties = find_peaks(
        rms,
        height=threshold,
        distance=150,
        prominence=0.02
    )

    # Keep only the strongest peaks if there are too many
    if len(peaks) > 15:
        strongest = np.argsort(properties["peak_heights"])[::-1][:15]
        peaks = peaks[strongest]
        peaks = np.sort(peaks)

    return times, rms, peaks