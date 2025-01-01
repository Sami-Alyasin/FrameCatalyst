from fastapi import FastAPI
from fastapi import Body
from google.cloud import texttospeech
import base64

# Create a FastAPI instance
app = FastAPI()

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from AI Video Generator backend!"}

# assign voice name for the project MVP
tts_voice_name = "en-US-Standard-I"


# Initialize the client at the top of the file
client = texttospeech.TextToSpeechClient.from_service_account_json("/Users/sami/projects/FrameCatalyst/secrets/framecatalyst-d4ad79d229a8.json")

# Define a TTS endpoint
@app.post("/tts")
def generate_tts(text: str = Body(...)):
    try:
        # Validate input length
        if len(text) > 500:
            return {"error": "Text too long. Please limit to 500 characters."}
        
        # Prepare TTS request
        synthesis_input = texttospeech.SynthesisInput(text=text)
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
    