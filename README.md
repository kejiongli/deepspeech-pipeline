# deepspeech-pipeline
Build pipeline for multichannel audio S2T JSON transcription 
and the expected JSON output.

Main features:
- Deal with different types of audio types including, .mp3, .mp4 
and different bits of .wav
- Deal with mono or multi-channel (>=2) audio files
- Produce different types of json transcriptions
        
     * word level json transcription per channel
     * sentence level json transcription per audio 
     (including start time, duration, and channel number)


Instruction

Windows OS:

1. install ffmpeg 

  Download: Go to http://ffmpeg.org/download.html#build-windows and select an appropriate windows version number
  
  Unzip it to a folder that’s easy to find, like directly to your C:\ drive. It should create a folder like ffmpeg-20170418-6108805-win64-static 
  
  Add the bin folder, which contains the ffmpeg.exe file, to your system 
path to allow us to run the commands easily.

Then cmd to try ffmpeg -version to check if it installed 

2. Set up python virtual environment and pip install requirments.txt

3. Download deepspeech pre-trained English model and extract

    curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz
    tar xvf deepspeech-0.6.1-models.tar.gz

    unzip the file and place them into "models" folder

4. Download example audio files
   
   curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/audio-0.6.1.tar.gz
   tar xvf audio-0.6.1.tar.gz
   
   unzip the file and place them into "samples/raw" folder
   
   FYI: You can also download other format audios, e.g. .mp3, .mp4 etc or multi-channel audios and place them into raw folder.
   
5. Run the main function - stt_main.py

   
   