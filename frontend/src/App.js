import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [audioSrc, setAudioSrc] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/tts',  // Correct endpoint
        { text },  // Send as regular JSON object, not stringified
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
      setAudioSrc(`data:audio/mp3;base64,${response.data.audio_base64}`);
    } catch (error) {
      console.error('Error generating TTS:', error);
    }
  };

  return (
    <div className="App">
      <h1>AI Video Generator</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter your text here to convert it to speech..."
          rows="6"
        />
        <button type="submit">Generate Speech</button>
      </form>
      {audioSrc && (
        <div className="audio-container">
          <h2>Generated Speech</h2>
          <audio controls src={audioSrc} />
        </div>
      )}
    </div>
  );
}

export default App;
