import torch
import os

from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
model = PretrainedSpeakerEmbedding(
    "speechbrain/spkrec-ecapa-voxceleb",
    device=torch.device("cpu"))

from pyannote.audio import Audio
from pyannote.core import Segment
audio = Audio(sample_rate=16000, mono="downmix")

# extract embedding for a speaker speaking between t=3s and t=6s
speaker1 = Segment(3., 120.)
waveform1, sample_rate = audio.crop("manal.wav", speaker1)
manal = model(waveform1[None])

# extract embedding for a speaker speaking between t=7s and t=12s
speaker2 = Segment(0., 2.)
waveform2, sample_rate = audio.crop("ben.wav", speaker2)
ben = model(waveform2[None])

# compare embeddings using "cosine" distance
from scipy.spatial.distance import cdist
distance = cdist(manal, ben, metric="cosine")
print(f"embedding1: {manal.shape}")
print(distance )
