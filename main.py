
import re
import os
import sys
from pathlib import Path
import argparse
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def len_regex_type(arg_value, pat=re.compile(r"^\d+:?\d*$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return float(".".join(arg_value.split(":")))

def size_regex_type(arg_value, pat=re.compile(r"^\d+.?\d{0,2}[KMG]?B$")):
    if not pat.fullmatch(arg_value):
        raise argparse.ArgumentTypeError
    
    units = {
        "KB": 1024,
        "MB": 1024**2,
        "GB": 1024**3
    }
    
    if arg_value[-2].isalpha():
        total = float(arg_value[:-2])*units[arg_value[-2:]]
    else:
        total = float(arg_value[:-1])
    return total

def ratio(an, ad, bn):
    return (ad*bn)/an

def read_inputs():
    parser = argparse.ArgumentParser('Trimming/Splitting Operations on Video Files')

    parser.add_argument('--file', nargs=1, metavar="FILENAME", type=str, required=True)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--len', nargs=1,  metavar="LENGTH - Format: mm[:ss]", type=len_regex_type)
    group.add_argument('--size', nargs=1,  metavar="SIZE - Format: dd...d[.dd]B|KB|MB|GB)", type=size_regex_type)

    # parser.print_help()

    args = parser.parse_args()
    filename = args.file[0]
    if not os.path.exists(filename):
        print(f"File Not Found Error: File '{filename}' not found in local.")
        sys.exit(0)
    clip = VideoFileClip(filename)
    
    length, size = 0.0, 0.0
    if args.len != None:
        number, decimal_part = map(int, str(args.len[0]).split("."))
        if decimal_part != 0:
            length = round(ratio(60, decimal_part, 100)/10, 2)
        length += number
    else:
        size = args.size[0]
        filesize = Path(filename).stat().st_size
        length = round(ratio(filesize, size, clip.duration), 2)

    return filename, length, clip.duration

def decimal_to_time(d):
    number, decimal = map(int, str(d).split("."))
    if decimal == 0:
        return str(number)+":00"
    return f"{number}:{str(int(ratio(100, decimal, 60)))[:2]}"
    
if __name__ == "__main__":
    filename, split_len, duration = read_inputs()
    splits = int(duration//split_len) +(1 if duration%split_len != 0 else 0)
    print(f"Filename: {filename}\nDuration: {decimal_to_time(duration)}\nLength of Split: {decimal_to_time(split_len)}\nNo. of Splits: {splits}")

    name, ext = os.path.splitext(filename)
    places = len(str(splits))
    start = 0.0
    for i in range(splits):
        split_name = f"{name} - Chunk {str(i+1).zfill(places)}{ext}"
        print(f"\nWriting chunk with name '{split_name}' from & to length [{decimal_to_time(start)}, {decimal_to_time(duration if i == splits-1 else start+split_len)}] of the actual file '{filename}' ...")
        ffmpeg_extract_subclip(filename, start, start+split_len, targetname=split_name)
        start += split_len
        print(f"Written chunk '{split_name}' successfully!!")
    
    print(f"\nAll {splits} chunks have successfully written into current directory.")