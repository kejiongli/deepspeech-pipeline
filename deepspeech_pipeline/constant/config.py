import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE_DIR = os.path.join(ROOT_DIR, '..' ,'models')

BEAM_WIDTH = 500
LM_ALPHA = 0.75
LM_BETA = 1.85

MODEL_FILE = os.path.join(MODEL_FILE_DIR, 'output_graph.pbmm')
LANGUAGE_MODEL = os.path.join(MODEL_FILE_DIR, 'lm.binary')
TRIE_FILE = os.path.join(MODEL_FILE_DIR, 'trie')