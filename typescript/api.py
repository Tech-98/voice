from flask import Flask, request
from flask_cors import CORS
import base64

index = 0
app = Flask(__name__)
CORS(
        app,
        resources={r"/*": {"origins": "*"}},
        headers=['Content-Type', 'X-Requested-With', 'Authorization']
    )
@app.route('/api/audio', methods=['POST'])
def receive_audio():
    global index
    # index += 1
    print("received audio")
    print(type(request.data))
    # print(request.data)
    audio_data = base64.b64decode(request.data)

    # Write binary data to a WAV file
    with open(f'received_audio{index}.wav', 'wb') as f:
        f.write(audio_data)
    # audio_file = request.files['audio']
    # # Process the audio file (save to disk, perform analysis, etc.)
    # # For demonstration, let's just save it to disk
    # audio_file.save(f'received_audio{index}.wav')
    return 'Audio received successfully'

if __name__ == '__main__':
    app.run(debug=True)  # Run Flask app in debug mode