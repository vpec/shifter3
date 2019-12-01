# shifter3 - Simple Subtitle Shifter

shifter3 is a simple python3 script that allows you to modify a .srt file, shifting its content by any desired time. You only have to provide any number (representing seconds), and all subtitles will be shifted by it.

## Usage
`$ shifter3 <SHIFT_IN_SECONDS> <INPUT_FILE> [<OUTPUT_FILE>]`

shifter3 accepts 2 or 3 arguments:

  - First argument: amount of time you want to shift the subtitles in the .srt file. It will be interpreted as seconds, and it can be a fractional number.
  - Second argument: your .srt input file. If no third argument is provided, shifter3 will overwrite your input file.
  - Third argument (OPTIONAL): your .srt ouput file. If this argument is provided, your input file will be left intact after the execution of this script.
  
## Examples
Subtitles in mysubtitles.srt show up too soon, I want all of them to start (and finish) 0.25 seconds later:

`$ shifter3 0.25 mysubtitles.srt`

Subtitles in mysubtitles.srt show up too late, I want all of them to start (and finish) 0.25 seconds before:

`$ shifter3 -0.25 mysubtitles.srt`


Subtitles in mysubtitles.srt show up too late, I want all of them to start (and finish) 1 second before AND get the result in a new file named myNEWsubtitles.srt:

`$ shifter3 -1 mysubtitles.srt myNEWsubtitles.srt`

## Installation
*Note: This instructions are aimed at Unix-based systems like Linux (Ubuntu, Debian, OpenSuse...) or Mac OS X, but they may also work in Windows if you use a Linux sub-system.*
1. Install Python (version 3). If you already have installed python3 in your machine, go to step 2. For installing python3, go to the [official Python website](https://www.python.org/downloads) and follow the instructions.
2. Clone the repository:
`$ git clone https://github.com/vpec/shifter3.git`.
Alternatively, you can download it as zip package and then uncompress it.
3. Enter the directory:
`$ cd shifter3`
4. After the download, you might not have execution permissions on the script. To fix this, execute `$ chmod u+x shifter3`. 
5. If you want to use this script from any directory in your system, you can add the shifter3 directory path to the system 's path. [This tutorial](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7) explains how to do it.
6. Now you can execute shifter3. If you didn't follow step number 5, you will have to execute the script from its directory using `$ ./shifter3` instead of `$ shifter3`
