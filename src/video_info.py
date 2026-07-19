import cv2
import os


def get_video_info(video_path):
    """
    Extract metadata from a video using OpenCV.
    """

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return None

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    duration = total_frames / fps if fps else 0

    cap.release()

    file_size = os.path.getsize(video_path) / (1024 * 1024)

    return {
        "duration": duration,
        "fps": fps,
        "width": width,
        "height": height,
        "size": file_size
    }