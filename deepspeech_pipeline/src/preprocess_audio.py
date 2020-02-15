"""
Convert different type of audios to .wav with sample rate 16000
Split multi-channel (>=2) audio to mono channel
"""
import os
import subprocess

from scipy.io import wavfile

SAMPLE_RATE = 16000

DIR_WAV = 'WAV'
DIR_CHANNEL = 'channels'

EXT_WAV = '.wav'


def convert_sample_rate(in_file, out_dir):
    out_wav_dir = os.path.join(out_dir, DIR_WAV)
    os.makedirs(out_wav_dir, exist_ok=True)

    output_wav = 'output'+ EXT_WAV
    output_wav_path = os.path.join(out_wav_dir, output_wav)


    cmd = ['ffmpeg', '-i', in_file, '-ar', str(SAMPLE_RATE), '-y', output_wav_path]
    subprocess.check_output(' '.join(cmd), shell=True)

    return output_wav_path


def split_channel(in_file, out_dir, nchannel):
    out_channel_dir = os.path.join(out_dir, DIR_CHANNEL)
    os.makedirs(out_channel_dir, exist_ok=True)
    sr, audio = wavfile.read(in_file)

    audio_length = len(audio)*(1/SAMPLE_RATE)

    channel_path=[]
    for idx in range(nchannel):
        ichannel_path = os.path.join(out_channel_dir, 'channel_{}.wav'.format(idx))
        wavfile.write(ichannel_path, sr, audio[:, idx])
        channel_path.append(ichannel_path)

    return channel_path, audio_length




