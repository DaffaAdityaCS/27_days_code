# firstly Install module in below
# pip install deepspeech==0.8.2
# pip install ipython
# pip install tensorflow-gpu

# get request from git repo below
# wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.2/deepspeech-0.8.2-models.pbmm
# wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.2/deepspeech-0.8.2-models.scorer

from deepspeech import Model
import numpy as np
import os
import wave

from IPython.display import Audio

model_file_path = 'deepspeech-0.8.2-models.pbmm'
lm_file_path = 'deepspeech-0.8.2-models.scorer'
beam_width = 500
lm_alpha = 0.93
lm_beta = 1.18

model = Model(model_file_path)
model.enableExternalScorer(lm_file_path)

model.setScorerAlphaBeta(lm_alpha, lm_beta)
model.setBeamWidth(beam_width)

def read_wav_file(filename):
  with wave.open(filename, 'rb') as w:
    rate = w.getframerate()
    frames = w.getnframes()
    buffer = w.readframes(frames)
    print(rate)
    print(frames)

  return buffer, rate

def transcribe(audio_file):
  buffer, rate = read_wav_file(audio_file)
  data16 = np.frombuffer(buffer, dtype=np.int16)
  return model.stt(data16)

# donwload the sample audio from repo
#wget -O speech.wav https://github.com/EN10/DeepSpeech/blob/master/woman1_wb.wav?raw=true

Audio('speech.wav')

transcribe('speech.wav')

#recommend doing in google colab to execute the code