
"""
Run deepspeech model
"""
import logging

from timeit import default_timer as timer
from deepspeech import Model
from scipy.io import wavfile

from deepspeech_pipeline.constant.config import MODEL_FILE, BEAM_WIDTH, TRIE_FILE, LM_ALPHA, LM_BETA, LANGUAGE_MODEL

SAMPLE_RATE = 16000
logging.basicConfig(level=logging.DEBUG)

def load_models():
    model_load_start = timer()
    ds = Model(MODEL_FILE, BEAM_WIDTH)
    model_load_end = timer() - model_load_start

    logging.debug('Loaded model in %0.3fs.' % (model_load_end))

    lm_load_start = timer()
    ds.enableDecoderWithLM(LANGUAGE_MODEL, TRIE_FILE, LM_ALPHA, LM_BETA)
    lm_load_end = timer() - lm_load_start

    logging.debug('Loaded language model in %0.3fs.' % (lm_load_end))

    return ds


def process_stt_meta(audio_path):
    ds = load_models()

    sr, audio = wavfile.read(audio_path)

    inferecne_time = 0.0
    audio_length = len(audio)*(1/SAMPLE_RATE)

    logging.debug('Running inference with stt result with meta')
    inference_start = timer()

    output_withmeta = ds.sttWithMetadata(audio)

    inference_end = timer() - inferecne_time
    inferecne_time += inference_end
    logging.debug('Inference took %0.3fs for %0.3fs audio file.' %(inference_end, audio_length))

    return output_withmeta


def process_stt_text(audio_path):
    ds = load_models()

    sr, audio = wavfile.read(audio_path)

    inferecne_time = 0.0
    audio_length = len(audio)*(1/SAMPLE_RATE)

    logging.debug('Running inference with stt result with text')
    inference_start = timer()

    output = ds.stt(audio)

    inference_end = timer() - inferecne_time
    inferecne_time += inference_end
    logging.debug('Inference took %0.3fs for %0.3fs audio file.' %(inference_end, audio_length))

    return output