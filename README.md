# MKVerything
Makes your library be remuxed to mkv.
# Remux Master 🎞️

A robust Bash script to batch convert (remux) legacy video containers (`.avi`, `.mp4`, `.ogm`, `.divx`) into clean, standardized `.mkv` files without transcoding.

## 🚀 Why use this?
Ideal for modernizing large media libraries (NAS, Plex, Jellyfin) before processing with tools like Tdarr. It fixes common container errors while preserving 100% of original video/audio quality.

## ✨ Features
* **Zero Quality Loss:** Uses `ffmpeg -c copy` by default.
* **Smart Fallbacks:**
    * 1️⃣ Tries direct copy.
    * 2️⃣ If that fails (e.g., `mov_text` subs), converts subtitles to SRT.
    * 3️⃣ If that fails (bitmap subs), drops subtitles to save the video.
    * 4️⃣ "Strict Mode": Drops cover art/attachments if they cause errors.
* **Safe:** Only deletes the original file after a successful verification.
* **Fast:** Skips files that are already converted.

## 🛠️ Usage
1.  Download `remux_master.sh`.
2.  Give execution permissions:
    ```bash
    chmod +x remux_master.sh
    ```
3.  Run it inside your media folder:
    ```bash
    ./MKVerything.sh
    ```

## 📋 Requirements
* Bash
* ffmpeg

## 📝 License
GNU AFFERO GENERAL PUBLIC LICENSE
