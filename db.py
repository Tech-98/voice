from scipy.spatial.distance import cdist
import torch
import os

from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
from pyannote.audio import Audio
from pyannote.core import Segment

class ModelSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.model = PretrainedSpeakerEmbedding("speechbrain/spkrec-ecapa-voxceleb", device=torch.device("cpu"))
        return cls._instance

class pyannote_db:
    instances = []
    # model = PretrainedSpeakerEmbedding(
    # "speechbrain/spkrec-ecapa-voxceleb",
    # device=torch.device("cpu"))

    def __init__(self, file):
        self.file = file
        self.name = file.split(".")[0].split("/")[-1]
        self.embeddings = self.get_embeddings(self.file)
        pyannote_db.instances.append(self)

    def get_embeddings(self, file):
        audio = Audio(sample_rate=16000, mono="downmix")
        duration = audio.get_duration(file)
        speaker = Segment(0., duration)
        waveform, sample_rate = audio.crop(file, speaker)
        embedding = ModelSingleton().model(waveform[None])
        return embedding
    def get_distance(self,input_embedding):
        return cdist(self.embeddings, input_embedding, metric="cosine")

    @classmethod
    def get_closest_distance(cls, file_to_compare):
        # print(f"Method called from instance {instance.name}")  # Access instance name
        embeddings = cls.get_embeddings(cls,file_to_compare)
        smallest_distance = float(2)
        closest_instance = None
        for inst in cls.instances:
            distance = round(inst.get_distance(embeddings)[0][0], 4)
            if distance < smallest_distance:
                smallest_distance = distance
                closest_instance = inst
        #     print(f"Distance between instance and {inst.name} is {distance}")
        # print(f"Closest instance to instance is {closest_instance.name} with distance {smallest_distance}")
        return closest_instance.name, smallest_distance