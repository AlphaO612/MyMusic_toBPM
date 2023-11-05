# MyMusic_toBPM
This script all custom music with format .mp3 or .wav prepare to ready custom music .wav for the game "BPM: Bullet Per Minutes" 
## What does its do?
This script(application) all music from /loads/* format .mp3 and .wav processing to wav, find bpm, check songs's bpm in period 60 - 120 bpm or not. 

If songs's bpm in period, song cutting from time of first beat until end of the song and exports to folder /loads/temp_wav/result.
Other songs what bm isn't period 60-120 skipping!

BUT you can turn off this function that is means, system ignore check bpm and export like others fine song!

## How to Use it?
We have 3 ways:
 - [Colab](https://github.com/AlphaO612/MyMusic_toBPM/blob/main/README.md#colab)
 - [Windows Method](https://github.com/AlphaO612/MyMusic_toBPM/blob/main/README.md#windows-method)
 - [Python 3.9 and latest version](https://github.com/AlphaO612/MyMusic_toBPM/blob/main/README.md#python-39-and-latest-version)
### Colab
This project has colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PScDuCS38axi4McQCLxsJRLbzw6JyexS?usp=sharing)

The disadvantage of this method is the low loading and downloading of music to and from colab. 
### Windows Method
1. Download latest release
2. Download ffmpeg
    - Open [github releases page ffmpeg](https://github.com/GyanD/codexffmpeg/releases)
    - download from latest releases file with name "ffmpeg-X.X-essentials_build.zip" when X.X is number of version
    - open this zip package
    - from folder **/ffmpeg-X.X-essentials_build/bin/*** copy to project "MyMusic_toBPM" about **main.exe**
4.   Load all your music _(only with format .mp3 or .wav and song duration more than 10 second)_ to `"/loads"` folder
5.   Start **main.exe**
     - Arguments Settings from console: (_example_: `main.exe --ignorelimits true` - this is means all song will be prepared without checking bpm limits )
       - `-h`, `--help` – show this help message and exit
       - `--pwd <PWD>` - Path(should only english alphabet and without Space) to work directory where storing all data for script(loads, venv, ffmpeg and etc.)
       - `--ignorelimits <IGNORELIMITS>` - Argument for ignore limits bpm(60-120) of the game and not skipping non-recommend bpm of your song
       - `--ffmpeg <FFMPEG>` - Path(should only english alphabet and without Space + ended 'ffmpeg.exe') to ffmpeg
       - `--ffprobe <FFPROBE>` - Path(should only english alphabet and without Space + ended 'ffprobe.exe') to ffprobe
7.   Open folder `/loads/temp_wav/result` with prepared music for BPM

THE END! 

### Python 3.9 and latest version
1. Load project on your local computer
   - Git clone: `git clone https://https://github.com/AlphaO612/MyMusic_toBPM.git`
   - Manually download from github.
3. Install all libs for python
    - `python -m pip install librosa pydub`
5. Download ffmpeg
    - Open [github releases page ffmpeg](https://github.com/GyanD/codexffmpeg/releases)
    - download from latest releases file with name "ffmpeg-X.X-essentials_build.zip" when X.X is number of version
    - open this zip package
    - from folder **/ffmpeg-X.X-essentials_build/bin/*** copy to project "MyMusic_toBPM" about **main.py**
6. Start `python main.py`
     - Arguments Settings from console: (_example_: `python main.py --ignorelimits true` - this is means all song will be prepared without checking bpm limits )
       - `-h`, `--help` – show this help message and exit
       - `--pwd <PWD>` - Path(should only english alphabet and without Space) to work directory where storing all data for script(loads, venv, ffmpeg and etc.)
       - `--ignorelimits <IGNORELIMITS>` - Argument for ignore limits bpm(60-120) of the game and not skipping non-recommend bpm of your song
       - `--ffmpeg <FFMPEG>` - Path(should only english alphabet and without Space + ended 'ffmpeg.exe') to ffmpeg
       - `--ffprobe <FFPROBE>` - Path(should only english alphabet and without Space + ended 'ffprobe.exe') to ffprobe
7.   Open folder `/loads/temp_wav/result` with prepared music for BPM

THE END!

You can copy one of stored folder (like 'Asgard1', 'Asgard2' and etc.) in `<path where steam installed>\Steam\steamapps\common\BPM BULLETS PER MINUTE\WindowsNoEditor\BPM\CustomSoundtrack\`.

# Contacts
Please report all issues in section 'Issues'.

Tg: [t.me/arefaste](https://t.me/arefaste)
Email: alphaste08@gmail.com

---
***~Cya!*** ❤️✨
