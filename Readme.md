# 🎬 AI YouTube Video Engine

An automated pipeline that converts text scripts into short AI-generated videos with background visuals, text overlays, and voice narration.

---

## 🚀 Features

* 🧠 Script-based video generation
* 🎨 Dynamic background selection based on topic
* ✍️ Custom text rendering using PIL (centered & wrapped properly)
* 🔊 Audio narration integration
* 🎞️ Scene-by-scene video composition using MoviePy
* 🧩 Modular and customizable pipeline

---

## 🛠️ Tech Stack

* Python
* MoviePy
* PIL (Pillow)
* NumPy

---

## 📂 Project Structure

```
├── assets/                # Background images
├── output/                # Generated videos (ignored in git)
├── main.py                # Main execution file
├── text_renderer.py       # Text rendering logic (PIL)
├── audio/                 # Audio files
├── README.md
```

---

## ⚙️ How It Works

1. Input a script (multi-line text)
2. Each line becomes a video scene
3. Background is selected based on topic
4. Text is rendered onto transparent image (PIL)
5. Audio is synced across scenes
6. Final video is generated using MoviePy

---

## ▶️ Usage

```bash
python main.py
```

Or call the function directly:

```python
generate_video(script, audio_path, topic)
```

---

## 🧪 Example

**Input Script:**

```
Ever wondered how we navigate through the cosmos?
Or what causes time dilation?
```

**Output:**

* Multi-scene video
* Centered text overlays
* Synced narration

---

## 🔧 Recent Improvements

* Fixed text centering and overflow issues
* Implemented proper text wrapping using PIL
* Improved visual alignment inside frame
* Cleaner video composition pipeline

---

## ⚠️ Notes

* Make sure fonts are available (e.g. Arial)
* Large media files should not be committed (use `.gitignore`)
* Audio duration is evenly split across script lines

---

## 📌 Future Improvements

* Better voice synthesis (more natural tone)
* Text animation (fade/slide effects)
* Scene transitions
* Subtitle-style timing instead of equal splits
* CLI interface for easier usage

---

## 🤝 Contribution

This project is experimental and evolving. Feel free to fork and improve.

---

## 📄 License

MIT License
