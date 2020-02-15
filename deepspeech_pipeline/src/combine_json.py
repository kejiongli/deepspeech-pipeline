"""Combine seperate mono channel json file into one and generate the expected combine json output"""

import json
import os

OUTPUT_FILE = 's2t_output.json'

def channel_continue(cur_channel_number, next_channel_number):
    if cur_channel_number == next_channel_number:
        return True
    else:
        return False


def generate_sentence(text_segments, channel_number):
    text = ' '.join(text_segment['Word'] for text_segment in text_segments)
    duration = sum(text_segment['Duration'] for text_segment in text_segments)

    start_time = text_segments[0]['StartTime']
    seg_dict = {"RecongitionStatus": "Success",
                "ChannelNumber": channel_number,
                "DurationInSeconds": duration,
                "OffsetInSeconds": start_time,
                "NBest": [{"Lexical": text}]
                }
    return seg_dict

def generate_combine_result(json_list, file_dir, audio_length, audio_name):
    sorted_list = sorted(json_list, key=lambda k : k['StartTime'])

    segment_results = []
    text_segments = []

    for idx, word in enumerate(sorted_list):
        cur_word_seg = sorted_list[idx]
        next_word_seg = sorted_list[idx+1] if idx+1< len(sorted_list) else None

        cur_channel_no = cur_word_seg['ChannelNumber']
        next_channel_no = next_word_seg['ChannelNumber'] if next_word_seg is not None else None

        if next_channel_no is not None and channel_continue(cur_channel_no, next_channel_no):
            text_segments.append(cur_word_seg)

        else:
            text_segments.append(cur_word_seg)
            segment_results.append(generate_sentence(text_segments, cur_channel_no))
            text_segments = []


    s2t_json = dict()
    s2t_json["AudioFileResults"] = [{
        "AudioFileName": audio_name,
        "AudioLengthInSeconds": audio_length,
        "SegmentResults": segment_results
    }]

    output_file_path = os.path.join(file_dir, OUTPUT_FILE)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(s2t_json, f, indent=2, ensure_ascii=False)
