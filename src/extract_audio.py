from moviepy import VideoFileClip
import os


def extract_audio(video_path):
    """
    Extract audio from the uploaded video and save it as WAV.
    """

    os.makedirs("data/audio", exist_ok=True)

    audio_path = os.path.join(
        "data/audio",
        "match_audio.wav"
    )

    video = VideoFileClip(video_path)

    video.audio.write_audiofile(
        audio_path,
        logger=None
    )

    video.close()

    return audio_path