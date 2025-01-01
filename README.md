# FrameCatalyst

**FrameCatalyst** is an AI-powered text-to-video generation tool. It transforms user-written text into dynamic, avatar-narrated videos with background stock footage, transitions, and more. This repository contains both the backend (AI services and video-processing logic) and the frontend (web interface) of the application.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
    - [Backend Setup](#backend-setup)
    - [Frontend Setup](#frontend-setup)
5. [Usage](#usage)
    - [Generate Text-to-Speech](#generate-text-to-speech)
    - [Lip-Sync and Avatar Integration](#lip-sync-and-avatar-integration)
    - [Stock Footage and Video Assembly](#stock-footage-and-video-assembly)
6. [Roadmap](#roadmap)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

---

## Overview

FrameCatalyst aims to simplify and automate the process of creating engaging video content for social media, marketing, and educational purposes. By combining advanced Text-to-Speech (TTS) models, lip-sync technologies, and automated video editing pipelines, FrameCatalyst enables you to produce polished, ready-to-publish videos with minimal effort.

Key functionalities include:
- Multiple language TTS
- Avatar-based lip-syncing
- Integration with stock footage libraries
- Automated editing and transitions
- Script generation and keyword extraction via LLMs (optional)

---

## Features

1. **Text-to-Speech (TTS):** Convert any user-provided text into natural-sounding speech in various languages and voices.
2. **Avatar Lip-Sync:** Use Wav2Lip or similar tools to sync your generated speech with a virtual avatar or a user-provided face video.
3. **Stock Footage Integration:** Search for and insert free or paid stock footage from providers (e.g., Pexels, Pixabay) to enrich your video segments.
4. **Automated Video Editing:** Combine TTS audio, lip-synced avatars, and background footage into a single video file using FFmpeg or MoviePy.
5. **Multi-Language Support:** Generate content in multiple languages by simply switching TTS language parameters.
6. **LLM-Based Script Assistance (Optional):** Leverage GPT-Neo, Llama 2, or other models to generate or analyze scripts and provide keyword recommendations for footage.

---

## Tech Stack

- **Backend:**
  - [FastAPI](https://fastapi.tiangolo.com/) or Flask (Python)
  - [Google Cloud TTS](https://cloud.google.com/text-to-speech) / [Coqui TTS](https://github.com/coqui-ai/TTS) (for custom TTS)
  - [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) for lip-sync
  - [MoviePy](https://github.com/Zulko/moviepy) or FFmpeg for video assembly
  - [Transformers](https://github.com/huggingface/transformers) for LLM-based features

- **Frontend:**
  - [Next.js](https://nextjs.org/) or [React](https://reactjs.org/)
  - [Tailwind CSS](https://tailwindcss.com/) or other styling frameworks (optional)

- **Other Services/Tools:**
  - [Pexels API](https://www.pexels.com/api/) or [Pixabay API](https://pixabay.com/api/docs/) for stock footage
  - Docker (for containerization and deployment)
  - AWS / GCP / Azure (for hosting, storage, and compute)

---

## Installation

### Backend Setup

1. **Clone the repository** and navigate to `backend/`:
   ```bash
   git clone https://github.com/Sami-Alyasin/FrameCatalyst.git
   cd FrameCatalyst/backend
   ```
2. **Create a virtual environment** and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables** (e.g., Google Cloud TTS credentials, Pexels API key). You can store them in a `.env` file or set them manually:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path_to_google_credentials.json"
   export PEXELS_API_KEY="your_pexels_api_key"
   ```
5. **Start the server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
6. **Verify** by visiting `http://localhost:8000` in your browser or using a tool like `curl` or Postman.

### Frontend Setup

1. **Navigate to the `frontend/` folder**:
   ```bash
   cd ../frontend
   ```
2. **Install Node.js dependencies**:
   ```bash
   npm install
   ```
3. **Run the development server**:
   ```bash
   npm run dev
   ```
4. **Open** [http://localhost:3000](http://localhost:3000) to see the FrameCatalyst frontend in your browser.

---

## Usage

Below are common flows:

### Generate Text-to-Speech

1. Navigate to the main page of the app.
2. Enter your script in the text area.
3. Select desired language/voice if applicable.
4. Click **“Generate TTS”** to receive an audio output.

### Lip-Sync and Avatar Integration

1. Upload a face video or select a pre-made avatar in the UI (if available).
2. Provide or select TTS audio generated previously.
3. Click **“Lip-Sync”** to produce a talking avatar video.

### Stock Footage and Video Assembly

1. Search for relevant stock footage via the built-in “Search Stock” feature.
2. Preview and select clips to use as your video background or cut-in sequences.
3. Combine your lip-synced avatar clip with the background footage via the **“Assemble Video”** action.
4. Download the final merged video or preview it directly in the app.

---

## Roadmap

1. **Version 1.0**
   - [ ] Text-to-Speech integration
   - [ ] Lip-sync with Wav2Lip
   - [ ] Basic UI for script input and audio playback
2. **Future Plans**
   - [ ] LLM-based script generation and analysis
   - [ ] Advanced video templates and transitions
   - [ ] Multi-language user interface
   - [ ] Subscription models and analytics dashboards
   - [ ] Automated GPU-based scaling and container orchestration

---

## Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository and create a new branch for your feature or bugfix.  
2. **Commit** your changes with clear and concise messages.  
3. **Push** to your branch and submit a **Pull Request**.  
4. Ensure your changes are covered with tests, if applicable.

We appreciate any feedback, bug reports, and feature requests. Check out the [Issues](https://github.com/YourUser/FrameCatalyst/issues) page for outstanding tasks and discussions.

---

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text). You are free to use, modify, and distribute this code under the terms of the GPLv3. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Project Maintainer**: Sami Alyasin   
    - **Email**: Sami_Alyasin@outlook.com
    - **GitHub**: [github.com/Sami-Alyasin](https://github.com/Sami-Alyasin)

Feel free to reach out with any questions or suggestions. I hope you find this tool helpful!

---