import streamlit as st
from src.utils import save_uploaded_file
from src.video_info import get_video_info
from src.extract_audio import extract_audio
from src.audio_analysis import analyze_audio
from src.plot_graph import plot_excitement_graph

st.set_page_config(
    page_title="CrowdPulse",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ CrowdPulse")
st.subheader("AI Football Match Highlight Generator")

uploaded_file = st.file_uploader(
    "Upload a football match",
    type=["mp4", "mov", "avi"]
)

if uploaded_file:

    video_path = save_uploaded_file(uploaded_file)
    info = get_video_info(video_path)

    st.divider()

    st.subheader("📊 Video Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Duration", f"{info['duration']:.2f} sec")
        st.metric("FPS", f"{info['fps']:.2f}")

    with col2:
        st.metric("Resolution", f"{info['width']} × {info['height']}")
        st.metric("File Size", f"{info['size']:.2f} MB")

    st.success("✅ Video uploaded successfully!")

    st.video(video_path)

    st.write("📁 Saved to:")
    st.code(video_path)

    st.divider()

    if st.button("🎵 Extract Audio"):

        with st.spinner("Extracting audio..."):

            audio_path = extract_audio(video_path)

        st.success("Audio extracted successfully!")

        st.audio(audio_path)

        times, rms, peaks = analyze_audio(audio_path)

        st.subheader("📈 Match Excitement Graph")

        fig = plot_excitement_graph(times, rms, peaks)

        st.pyplot(fig)    

        st.subheader("🔥 Detected Exciting Moments")

        for i, peak in enumerate(peaks):

            total_seconds = int(times[peak])

            minutes = total_seconds // 60
            seconds = total_seconds % 60

            st.write(f"⚽ Moment {i+1}: {minutes:02d}:{seconds:02d}")