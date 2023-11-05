import json
import os, librosa, argparse
from pydub import AudioSegment


class Song:
    def __init__(self, path: str, automatic_check: bool = True):
        self.path = path
        self._under_path, self.filename = os.path.split(self.path)
        if automatic_check:
            self._load_music()


    def check_format(self, is_format: str = "wav"):
        return self.filename.split('.')[-1] == is_format

    def to_wav(self):
        if "mp3" in self.filename.split(".")[-1]:
            sound = AudioSegment.from_mp3(self.path)
            sound.export(f'{self._under_path}/temp_wav/{self.filename.split(".")[0]}.wav', format="wav")
            return Song(f'{self._under_path}/temp_wav/{self.filename.split(".")[0]}.wav')
        else:
            return self

    def _load_music(self):
        self._y, self._sr = librosa.load(self.path)

    def get_bpm(self):
        self.tempo, self.beat_frames = librosa.beat.beat_track(y=self._y, sr=self._sr)
        return self.tempo

    def get_beattimes(self, num_times: int = 0):
        data = librosa.frames_to_time(self.beat_frames, sr=self._sr)
        return data if not num_times else data[0:1+num_times]

    def to_result(self):
        newAudio = AudioSegment.from_wav(self.path)
        newAudio = newAudio[int(self.get_beattimes()[0]*1000): newAudio.duration_seconds*1000]
        arr = self.filename.split(".")
        new_filename = "{} {}bpm.wav".format(arr[0].replace(' ','_'), int(self.get_bpm()))
        newAudio.export(f'{self._under_path}/result/{new_filename}', format="wav")

        return Song(f'{self._under_path}/result/{new_filename}', automatic_check=False)

class App:
    def __init__(self, path: str = None, ignore_bpm: bool = False):
        if not path:
            path = os.getcwd()

        self.ignore_bpm = ignore_bpm
        self.path = path+"/loads/"

    def get_arr_files(self):
        return [f.name for f in os.scandir(self.path) if f.is_file()]

    def transformToSong(self, arr):
        result = []
        for name in (name for name in arr if name.split('.')[-1] in ["wav","mp3"]):
            song = Song(self.path + name).to_wav()
            _bpm = song.get_bpm()
            if 60 < _bpm < 120 or self.ignore_bpm:
                song = song.to_result()
                result.append(song)
            else:
              print('!warning! - SONG MISSED! ', int(_bpm),'bpm is not in period 60-120 bpm for song -> ', name)

        return result

    def get_names_arr(self, arr):
        return [song.filename for song in arr]


def some_process():
    parser = argparse.ArgumentParser(description="Process .wav or .mp3 file for comfort play BPM: Bullet Per Minutes.")
    parser.add_argument("--pwd", default=None, help="work directory where storing all data for script(loads, venv, ffmpeg and etc.)")
    parser.add_argument(
        "--ignorelimits",
        type=bool,
        default=False,
        help="Argument for ignore limits bpm(60-120) of the game and not skipping non-recommend bpm of your song",
    )
    parser.add_argument(
        "--ffmpeg",
        type=str,
        default="ffmpeg.exe",
        help="Path to ffmpeg",
    )
    parser.add_argument(
        "--ffprobe",
        type=str,
        default='ffprobe.exe',
        help="Path to ffprobe",
    )
    args = parser.parse_args()

    AudioSegment.converter = args.ffmpeg
    AudioSegment.ffprobe = args.ffprobe
    print(args)
    app = App(args.pwd, ignore_bpm=args.ignorelimits)
    print("="*10,"started process","="*10)
    print("ALL SONG in 'result' folder:\n - "+"\n - ".join(app.get_names_arr(app.transformToSong(app.get_arr_files()))))


if __name__ == '__main__':
    some_process()
    input("application finished!\n - Press any button on the your keyboard to close application...")
