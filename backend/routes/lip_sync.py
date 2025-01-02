# routes/lip_sync.py
from fastapi import APIRouter, UploadFile, File
import uuid
import subprocess
from pydub import AudioSegment

router = APIRouter()

@router.post("/")
def lip_sync_endpoint(audio_file: UploadFile = File(...), face_file: UploadFile = File(...)):
    """
    Accepts audio and face video files, runs Wav2Lip, and returns the output video file path.
    """

    # 1) Save uploaded files temporarily
    audio_temp = f"temp_{uuid.uuid4()}.mp3"
    with open(audio_temp, "wb") as f:
        f.write(audio_file.file.read())

    face_temp = f"temp_{uuid.uuid4()}.mp4"
    with open(face_temp, "wb") as f:
        f.write(face_file.file.read())

    # 2) Convert MP3 -> WAV
    wav_path = audio_temp.replace(".mp3", ".wav")
    AudioSegment.from_mp3(audio_temp).export(wav_path, format="wav")

    # 3) Run Wav2Lip inference
    output_video_path = f"lip_sync_result_{uuid.uuid4()}.mp4"
    command = [
        "python", "Wav2Lip/inference.py",
        "--face", face_temp,
        "--audio", wav_path,
        "--outfile", output_video_path
    ]
    subprocess.run(command, check=True)

    return {"lip_synced_video": output_video_path}
