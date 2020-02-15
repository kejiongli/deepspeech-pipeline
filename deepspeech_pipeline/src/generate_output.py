"""The process to extract each word from deepspeech meta object"""

import os
import json

DIR_TRANSCRIPTION = 'transcription'

EXT_JSON = '.json'
EXT_TXT = '.txt'

def save_metadata_json(metadata, channel_idx, out_parent_dir):
    out_json_dir = os.path.join(out_parent_dir, DIR_TRANSCRIPTION)
    os.makedirs(out_json_dir, exist_ok=True)

    output_json_file = 'channel_' + str(channel_idx) + EXT_JSON
    output_json_path = os.path.join(out_json_dir, output_json_file)

    json_result = dict()
    json_result['Words'] = words_from_metadata(metadata, channel_idx)
    json_result['Confidence'] = metadata.confidence

    with open(output_json_path, 'w') as f:
        json.dump(json_result, f, indent=2)

    return json_result['Words']


def words_from_metadata(metadata, channel_idx):
    word = ""
    word_list = []
    word_start_time = 0
    # Loop through each character
    for i in range(0, metadata.num_items):
        item = metadata.items[i]
        # Append character to word if it's not a space
        if item.character != " ":
            if len(word) == 0:
                # Log the start time of the new word
                word_start_time = item.start_time

            word = word + item.character
        # Word boundary is either a space or the last character in the array
        if item.character == " " or i == metadata.num_items - 1:
            word_duration = item.start_time - word_start_time

            if word_duration < 0:
                word_duration = 0

            each_word = dict()
            each_word['ChannelNumber'] = channel_idx
            each_word['Word'] = word
            each_word['StartTime'] = round(word_start_time, 4)
            each_word['Duration'] = round(word_duration, 4)

            word_list.append(each_word)
            # Reset
            word = ""
            word_start_time = 0

    return word_list
