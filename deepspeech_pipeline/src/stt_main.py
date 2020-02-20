"""Main interface to run deepspeech E2E pipeline"""

import os
import logging

from scipy.io import wavfile

from preprocess_audio import convert_sample_rate, split_channel
from run_deepspeech import process_stt_meta
from generate_output import save_metadata_json
from combine_json import generate_combine_result

OUTPUT_DIR = 'results'

SAMPLE_RATE = 16000

logging.basicConfig(level=logging.DEBUG)

def run_stt(top_dir):
    for root, dirs, files in os.walk(top_dir, topdown=False):

        base_dir = os.path.dirname(root)

        for fname in files:
            logging.info(f'{fname} in process')

            file_path = os.path.join(root, fname)
            file_name_path = os.path.splitext(file_path)[0]
            file_ext = os.path.splitext(file_path)[1].lower()
            file_base = os.path.basename(file_name_path)

            file_dir = os.path.join(base_dir, OUTPUT_DIR, file_base)

            os.makedirs(file_dir, exist_ok=True)

            logging.info('Step 1 Converting to an acceptable audio requirment for deepspeech')
            output_wav_path = convert_sample_rate(file_path, file_dir)
            sr, audio = wavfile.read(output_wav_path)

            assert sr == SAMPLE_RATE, f'Convert Sample Rate {sr} is not equal to {SAMPLE_RATE}'

            logging.info('Step 2 Splitting channel if needed')
            if audio.ndim >1:
                audio_channel_path, audio_length = split_channel(output_wav_path, file_dir, audio.ndim)
            else:
                audio_length = len(audio)*(1/SAMPLE_RATE)
                audio_channel_path = [output_wav_path]


            logging.info('Step 3 Run deepspeech per channel')
            json_result =[]

            for channel_idx, channel in enumerate(audio_channel_path):
                logging.info(f'processing channel {channel_idx}')

                stt_output_meta = process_stt_meta(channel)

                logging.info(f'saving channel {channel_idx}')
                json_result.extend(save_metadata_json(stt_output_meta, channel_idx, file_dir))

            logging.info("Step 4 - Combine Json File")
            generate_combine_result(json_result, file_dir, audio_length, fname)

            logging.info('{fname} audio process complete')


if __name__ == '__main__':
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    AUDIO_DATA_DIR = os.path.join(CUR_DIR, '..', 'samples', 'raw')
    # AUDIO_DATA_DIR = r'D:\kejiong\deepspeech-pipeline\deepspeech_pipeline\samples\raw'
    run_stt(AUDIO_DATA_DIR)
