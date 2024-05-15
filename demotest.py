import soundfile as sf
import pyaudio
import numpy as np
from db import pyannote_db
import os

SAMPLE_RATE = 16000
FRAMES_PER_BUFFER = 16000  # Use the same value as SAMPLE_RATE for consistency
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

test_directory = r"test_data/"
train_directory = r"train_data/"
directory = r"saif/"
passed = 0
failed = 0

voices = []

# manal_obj = pyannote_db(train_directory+ "manal.wav")
# ben_obj = pyannote_db(train_directory+ "ben.wav")
# saif_obj = pyannote_db(train_directory+ "saif.wav")
# cian_obj = pyannote_db(train_directory+ "cian.wav")
# shaheer_obj = pyannote_db(train_directory+ "shaheer.wav")
# azraa_obj = pyannote_db(train_directory+ "azraa.wav")
print("Recording init")
# starts recording
stream = p.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER
)

chunk_index = 0
def diarise_loop():
    while True:
        print("Recording started")
        # chunk_index += 1
        data = stream.read(int(FRAMES_PER_BUFFER * 2))
        data_s16 = np.frombuffer(data, dtype=np.int16)
        float_data = data_s16 * 0.5**15
        sf.write('chunk/chunk'+str(chunk_index)+'.wav', float_data, SAMPLE_RATE)  # Specify SAMPLE_RATE here
        name, distance = pyannote_db.get_closest_distance(str('chunk/chunk'+str(chunk_index)+'.wav'))
        if distance > 0.65 and distance < 0.85:
            name = f"Unknown closest match: {name}"
        if distance > 0.85:
            name = "Unknown/noise"
        print(f"Name: {name}, Distance: {distance}")

def diarise():
    data = stream.read(int(FRAMES_PER_BUFFER * 2))
    data_s16 = np.frombuffer(data, dtype=np.int16)
    float_data = data_s16 * 0.5**15
    sf.write('chunk/chunk'+str(chunk_index)+'.wav', float_data, SAMPLE_RATE)  # Specify SAMPLE_RATE here
    name, distance = pyannote_db.get_closest_distance(str('chunk/chunk'+str(chunk_index)+'.wav'))
    if distance > 0.75 and distance < 0.85:
        name = f"Unknown closest match: {name}"
    if distance > 0.85:
        name = "Unknown/noise"
    return f"Name: {name}, Distance: {distance}"

def add_record(name):
    global voices
    voices.append(pyannote_db(train_directory +str(name)+".wav"))

def add_train_data():
    global voices
    for file in os.listdir(train_directory):
        print(f"adding {file}")
        voices.append(pyannote_db(train_directory + file))

add_train_data()