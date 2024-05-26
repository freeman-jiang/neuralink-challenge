from pathlib import Path
from typing import Union

from pydub import AudioSegment


def convert_wav_to_flac(wav_file: Union[str, Path], flac_file: Union[str, Path]) -> None:
    """
    Converts a wav file to flac format.

    Args:
        wav_file (str or Path): Path to the input wav file.
        flac_file (str or Path): Path to the output flac file.
    """
    wav_file = Path(wav_file)
    flac_file = Path(flac_file)

    # read the wav file and export as flac
    song = AudioSegment.from_wav(wav_file)
    song.export(flac_file, format="flac")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("usage: python main.py <path_to_wav_file> <path_to_flac_file>")
        sys.exit(1)

    wav_file = sys.argv[1]
    flac_file = sys.argv[2]

    convert_wav_to_flac(wav_file, flac_file)
    print(f"converted {wav_file} to {flac_file}")
