// TypeScript code for the client-side web page

// Function to send chunks of audio data to the server
async function sendAudioChunk(chunk: Blob) {
    const formData = new FormData();
    formData.append('audio', chunk, 'audio.wav');
  
    try {
      const response = await fetch('http://localhost:5000/api/audio', {
        method: 'POST',
        body: formData
      });
  
      if (!response.ok) {
        throw new Error('Failed to send audio chunk to server');
      }
    } catch (error) {
      console.error('Error sending audio chunk:', error);
    }
  }
  
  // Function to start capturing audio from the microphone
  function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(mediaStream => {
        const mediaRecorder = new MediaRecorder(mediaStream);
        mediaRecorder.ondataavailable = (event) => {
          sendAudioChunk(event.data);
        };
        mediaRecorder.start();
      })
      .catch(error => {
        console.error('Error accessing microphone:', error);
      });
  }
  
  // Start recording when the page loads
  window.onload = () => {
    console.log("start recording")
    startRecording();
  };