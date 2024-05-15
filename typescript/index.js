// JavaScript code for the client-side web page

function blobToBase64(blob,mimeType) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(new Blob([blob], { type: mimeType }));
    reader.onloadend = () => {
      resolve(reader.result.split(',')[1]);
    };
    reader.onerror = reject;
  });
}
// Function to send chunks of audio data to the server
async function sendAudioChunk(chunk) {
  const formData = new FormData();
  formData.append('audio', chunk, 'audio.wav');
  var file = await blobToBase64(formData, 'audio/webm;codecs=opus')
  console.log(file)
  console.log("chunk:", chunk)
  try {
    console.log("trying to send chunk")
    const response = await fetch('http://localhost:5000/api/audio', {
      method: 'POST',
      body: file
    });
    console.log(response)
    if (!response.ok) {
      throw new Error('Failed to send audio chunk to server');
    }
  } catch (error) {
    console.error('Error sending audio chunk:', error);
  }
}

// Function to start capturing audio from the microphone
function startRecording() {
  console.log("trying to start")
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(function(mediaStream) {
      console.log("got mediastream", mediaStream)
      const mediaRecorder = new MediaRecorder(mediaStream);
      mediaRecorder.ondataavailable = function(event) {
        console.log("got data", event.data)
        sendAudioChunk(event.data);
      };
      mediaRecorder.start(3000);
    })
    .catch(function(error) {
      console.error('Error accessing microphone:', error);
    });
}

// Start recording when the page loads
window.onload = function() {
  startRecording();
  console.log("started")
};