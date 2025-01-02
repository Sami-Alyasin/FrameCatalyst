from fastapi import FastAPI
from fastapi import Body
from fastapi import APIRouter, UploadFile, File
from google.cloud import texttospeech
import base64
from pydantic import BaseModel
import os


router = APIRouter()

# assign voice name for the project MVP
tts_voice_name = "en-US-Standard-I"


# Initialize the client at the top of the file
client = texttospeech.TextToSpeechClient.from_service_account_json(
    os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
)

class TextRequest(BaseModel):
    text: str

# Define a TTS endpoint
@router.post("/tts")
def generate_tts(request: TextRequest):
    try:
        # Validate input length
        if len(request.text) > 500:
            return {"error": "Text too long. Please limit to 500 characters."}
        
        # Prepare TTS request
        synthesis_input = texttospeech.SynthesisInput(text=request.text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
            name = tts_voice_name
        )
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

        # Generate speech
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )
        
        # Base64 encode the audio content
        audio_base64 = base64.b64encode(response.audio_content).decode("utf-8")
        
        # Return the Base64-encoded audio
        return {"audio_base64": audio_base64}
    
    except Exception as e:
        print("Error during TTS generation:", e)
        return {"error": "Internal Server Error. Check server logs for details."}, 500
    