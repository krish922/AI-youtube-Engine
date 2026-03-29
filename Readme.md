# 🎬 AI YouTube Engine

A simple end-to-end pipeline that automatically generates short videos using:

* Topic Generation
* Script Generation
* Voice Synthesis
* Video Rendering

---

## 🚀 Overview

This project demonstrates how to build an **automated content generation system** using Python.

Pipeline flow:

```
Topic → Script → Voice → Video (.mp4)
```

The system works fully offline (without API), with optional support for AI-based script generation.

---

## ⚙️ Features

* ✅ Automatic topic generation
* ✅ Dynamic script creation (local mode)
* ✅ Text-to-speech using gTTS
* ✅ Video generation using MoviePy
* ✅ Modular pipeline structure
* ✅ Easy to extend with AI APIs (OpenAI / Kimi)

---

## 📁 Project Structure

```
AI-youtube-Engine/
│
├── src/
│   ├── topic.py               # Topic generator
│   ├── script_generator.py   # Script logic (local / AI)
│   ├── voice_generator.py    # gTTS voice generation
│   ├── video_builder.py      # Video creation
│   └── pipeline.py           # Connects everything
│
├── outputs/                  # Generated files (video/audio)
├── app.py                    # Entry point
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/AI-youtube-Engine.git
cd AI-youtube-Engine
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

```
python app.py
```

---

## 🎯 Output

After running, the system generates:

* 🎧 Audio file (`.mp3`)
* 🎬 Video file (`.mp4`)

Saved in your project directory.

---

## 🧠 How It Works

### 1. Topic Generator

Creates a random or predefined topic.

---

### 2. Script Generator

Generates a short script based on topic.

* Local Mode → Uses predefined templates
* AI Mode (optional) → Uses API (OpenAI / Kimi)

---

### 3. Voice Generator

Converts script → speech using gTTS.

---

### 4. Video Builder

* Creates background frame
* Adds text
* Syncs with audio
* Exports final video

---

## 🔁 Pipeline Flow

```
run_pipeline()

→ get_topic()
→ generate_script()
→ generate_voice()
→ generate_video()
```

---

## ⚡ Optional: AI Mode

To enable AI-based script generation:

1. Add API key (OpenAI / Kimi)
2. Update `script_generator.py`
3. Switch mode:

```
USE_AI = True
```

⚠️ API usage may require billing.

---

## 🧪 Development Mode

The project runs fully without API using:

```
USE_AI = False
```

This ensures:

* No external dependency
* Easy testing
* Stable execution

---

## 🚧 Future Improvements

* Better video styling (backgrounds, animations)
* Subtitle timing sync
* Multi-video batch generation
* YouTube auto-upload
* Thumbnail generation

---

## 🤝 Contribution

Feel free to fork and improve the project.

---

## 📌 Note

This project is a **learning + experimentation system**
for building AI-driven content pipelines.

---

## ⭐ If you like this project

Give it a star ⭐ and build your own engine.
