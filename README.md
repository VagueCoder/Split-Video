# :warning: `This is still under development!!`
# Split-Video
Just splits/trims video as per command line inputs. Nothing creative! Idea is to avoid website or desktop software usage (which mostly include costs after certain point) and make use of simple CLI tool.

## Technology/Tools Used
The following versions used in the process of development. However, for executing, you don't essentially need same versions.
Sno. | Technology | Version
----:|:----------:|:------:
1 | Python | 3.8.5
2 | Git | 2.25.1
3 | VScode | 1.56.2 x64
4 | GNU Make | 4.2.1
5 | Operating System | Windows 10 Pro WSL Ubuntu 20.04.2 LTS x86_64

## Imported Packages
The list of installed packages are in [requirements.txt](requirements.txt) file. However, important packages to focus on, are:
Sno. | Package | Version | Comment
----:|:-------:|:-------:|:-------
1 | moviepy | 1.0.3 | This is for video editing: cutting, concatenations, title insertions, video compositing, video processing, and creation of custom effects.
2 | virtualenv | 20.4.7 | A tool for creating isolated virtual python environments.

## Setup
Pretty simple! Just follow these steps:
1. Clone the repo or just download the zip as per will.
2. If you wish to use virtual environment (recommended), do the following. Else, skip to step-3.
```
python3 -m virtualenv venv
source venv/bin/activate
```
`Note`: Command for activating virtual env is not the same on Windows.

3. Install the required packages.
```
pip install -r requirements.txt
```
Once this is done, you're done with setup. Jump to usage section.

## Usage
Running could be done in either ways below. Let's start with help.
```
./split_vid.py -h
python3 split_vid.py -h
```
The help gives the tags you can use to split and the format of inputs.

Split by specifying the length of each split:
```
python split_vid.py --file sample.mp4 --len 62:50
```

Split by specifying the size of each split file (in Bytes, Kilo Bytes, Mega Bytes, Giga Bytes):
```
python split_vid.py --file sample.mp4 --size 2MB
```
`Note`: You should input either length or size to run.

## [Makefile](Makefile)
If GNU Make is available, checkout the [Makefile](Makefile) for commands and shortcuts. All the tasks that are used in development are included.

## Message to Viewer
A geek to geek: When this is useful to someone, I'd be glad. But if you want to add more interesting stuff to this, I very much encourage it. This is all yours to use!

Write to me at (Click): [VagueCoder0to.n@gmail.com](mailto:VagueCoder0to.n@gmail.com?subject=%5BGITHUB%3A%20Split-Video%5D%20Your%20Subject%20Here&body=Hello%20Vague%2C%0A%0A)

## Happy Coding !! :metal: