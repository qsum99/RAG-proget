# Quantum Information RAG Assistant (Quantum Tutor)

This project is a Retrieval-Augmented Generation (RAG) assistant for a Coursera course on Quantum Information and Communication. It allows users to ask questions about course content and receive detailed, timestamped answers referencing specific video segments.

## Features

- Converts video lectures to audio and transcribes them using OpenAI Whisper.
- Chunks and embeds subtitles for semantic search.
- Uses Google Gemini for embedding and answer generation.
- Flask web interface for interactive Q&A.
- Guides users to relevant videos, modules, and timestamps.

## Project Structure

```
.
├── buliding_flaskfremwrok         # Flask web app for chat interface
├── buliding_modle.py              # Script for local Q&A (CLI)
├── chunks_to_vec.py               # Converts subtitle chunks to embeddings
├── creting_chunks.py              # Transcribes audio and creates subtitle chunks
├── embeddings.joblib              # Precomputed embeddings for semantic search
├── mp4_to_mp3.py                  # Converts video files to audio
├── pulling_chunks.py              # Alternate script for Q&A
├── jsons/                         # Subtitle chunks in JSON format
├── templates/
│   └── index.html                 # Web UI template
├── video/                         # Source video files
├── video_mp3/                     # Converted audio files
├── whisper/                       # Whisper model files and changelog
└── .idea/                         # IDE config
```

## Setup

1. **Clone the repository**  
   ```sh
   git clone <>
   cd <>
   ```

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

   Make sure you have:
   - `openai-whisper`
   - `flask`
   - `joblib`
   - `scikit-learn`
   - `numpy`
   - `google-genai`

3. **Prepare Data**
   - Place your course videos in the `video/` directory.
   - Run `mp4_to_mp3.py` to extract audio.
   - Run `creting_chunks.py` to transcribe and chunk subtitles.
   - Run `chunks_to_vec.py` to generate embeddings and save as `embeddings.joblib`.

4. **Set up Google Gemini API**
   - Replace the API key in your scripts with your own Google Gemini API key.

## Usage

### Web Interface

Start the Flask app:

```sh
python buliding_flaskfremwrok
```

Open [http://localhost:5000](http://localhost:5000) in your browser and ask questions about the course.

### Command Line

Run:

```sh
python buliding_modle.py
```

Type your question when prompted.

## Example Question

> "Where is quantum teleportation taught?"

The assistant will respond with the relevant video/module, summary, and timestamped pointers.

## Notes

- Only questions related to the course content will be answered.
- Timestamps are converted to minutes for easier navigation.

## License

MIT License

---

**Contributors:**  
- Someshwar Kumbar
