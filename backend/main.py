from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routes.lip_sync import router as lip_sync_router  # Comment this out for now
from routes.tts import router as tts_router


# Create a FastAPI instance
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Changed from 3001 to 3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tts_router, tags=["Text-to-Speech"])
# app.include_router(lip_sync_router, tags=["Lip Sync"])  # Comment this out for now

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from AI Video Generator backend!"}

