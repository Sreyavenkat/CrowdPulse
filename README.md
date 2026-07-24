# ⚽ CrowdPulse

> **An AI-powered football match highlight generator that identifies exciting moments using crowd audio analysis and automatically generates highlight clips.**

CrowdPulse is a personal AI project that aims to reduce the time required to watch an entire football match by automatically detecting exciting moments and generating short highlight clips.

The project is currently under development. The current version analyzes crowd excitement from match audio, detects high-energy moments, and generates highlight clips. Future versions will incorporate AI-based commentary understanding to improve event detection and highlight accuracy.

---

## ✨ Current Features

* Upload football match videos
* Display video metadata

  * Duration
  * Resolution
  * FPS
  * File size
* Extract audio from uploaded videos
* Analyze crowd excitement using RMS energy
* Detect excitement peaks
* Visualize excitement using a graph
* Generate highlight clips around detected moments
* Interactive Streamlit interface

---

## 🚧 Planned Features

* Commentary transcription using OpenAI Whisper
* Goal, penalty, save, and card detection
* AI confidence scoring
* Intelligent event ranking
* Interactive match timeline
* Downloadable combined highlight reel
* Match statistics dashboard
* Plotly-based interactive visualizations

---

## 🛠 Tech Stack

**Language**

* Python

**Frontend**

* Streamlit

**Computer Vision & Video**

* OpenCV
* FFmpeg

**Audio Processing**

* Librosa
* NumPy
* SciPy

**Visualization**

* Matplotlib

**AI (Work in Progress)**

* OpenAI Whisper

---

## 📂 Project Structure

```text
CrowdPulse/
│
├── app.py
├── requirements.txt
│
├── src/
│   ├── utils.py
│   ├── video_info.py
│   ├── extract_audio.py
│   ├── audio_analysis.py
│   ├── plot_graph.py
│   ├── highlight_generator.py
│   ├── transcribe.py
│   └── commentary_analysis.py
│
├── data/
│   ├── uploads/
│   ├── audio/
│   └── highlights/
│
└── assets/
```

---

## 🔄 Current Workflow

```text
Upload Match Video
        │
        ▼
Extract Audio
        │
        ▼
Analyze Crowd Excitement
        │
        ▼
Detect Audio Peaks
        │
        ▼
Generate Highlight Clips
```

---

## 🎯 Project Goal

The long-term goal of CrowdPulse is to combine crowd audio analysis and AI-powered commentary understanding to automatically identify key football events and generate accurate, watchable match highlights.

---

## 📌 Project Status

**Current Version:** MVP (Minimum Viable Product)

**Completed**

* Video upload
* Audio extraction
* Excitement analysis
* Peak detection
* Highlight generation

**In Progress**

* Whisper transcription
* Commentary event detection
* AI confidence engine
* Enhanced UI and dashboard

---

## 👩‍💻 Author

**Sreya V**

B.Tech Computer Science and Engineering

Government Model Engineering College (MEC), Kerala
