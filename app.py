import streamlit as st
from src.utils import save_uploaded_file

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

    st.success("Video uploaded successfully!")

    st.video(video_path)

    st.write("📁 Saved to:")
    st.code(video_path)