# TODO: Implement the commented snippet in actual code below.
# import os
# import sys
# import argparse
# from moviepy.editor import VideoFileClip

# parser = argparse.ArgumentParser('Trimming/Splitting Operations on Video Files')
# parser.add_argument('--file', nargs=1)

# filename = parser.parse_args().file[0]

# if not os.path.exists(filename):
#     print(f"File Not Found Error: File '{filename}' not found in local.")
#     sys.exit(0)
# clip = VideoFileClip(filename)

# print(clip.duration)


import re
import argparse

def len_from_size(total:int, size:float) -> float:
    # TODO: Get the fraction and return start-end pairs rather than float value.
    return 0

units = {
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3
}

def len_regex_type(arg_value, pat=re.compile(r"^\d+:?\d*$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError
    return float(".".join(arg_value.split(":")))

def size_regex_type(arg_value, pat=re.compile(r"^\d+.?\d{0,2}[KMG]?B$")):
    if not pat.fullmatch(arg_value):
        raise argparse.ArgumentTypeError
    
    total = 0
    
    if arg_value[-2].isalpha():
        total = float(arg_value[:-2])*units[arg_value[-2:]]
    else:
        total = float(arg_value[:-1])
    return total

parser = argparse.ArgumentParser('Trimming/Splitting Operations on Video Files')

parser.add_argument('--file', nargs=1, metavar="FILENAME", type=str, required=True)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--len', nargs=1,  metavar="LENGTH (mm[:ss])", type=len_regex_type)
group.add_argument('--size', nargs=1,  metavar="SIZE (dd...d[.dd]B|KB|MB|GB)", type=size_regex_type)

parser.print_help()

args = parser.parse_args()
filename = args.file[0]
length, size = 0.0, 0.0
if args.len != None:
    length = args.len[0]
else:
    size = args.size[0]
    # TODO: As per len_from_size(), make changes here to receive the start-end pairs than just length of split.
print(f"Filename: {filename}\nLength: {length}\nSize: {size}")