# shifter3 - Simple Subtitle Shifter

shifter3 is a simple python3 script that allows you to modify a .srt file, shifting its content by any desired time. You only have to provide any number (representing seconds), and all subtitles will be shifted by it.

## Usage
`$ shifter3 <SHIFT_IN_SECONDS> <INPUT_FILE> [<OUTPUT_FILE>]`

shifter3 accepts 2 or 3 arguments:

  - First argument: amount of time you want to shift the subtitles in the .srt file. It will be interpreted as seconds, and it can be a fractional number.
  - Second argument: your .srt input file. If no third argument is provided, shifter3 will overwrite your input file.
  - Third argument (OPTIONAL): your .srt ouput file. If this argument is provided, your input file will be left intact after the execution of this script.
  
## Examples
Subtitles in mysubtitles.srt show up too soon, I want all of them to start 0.25 seconds later:

`$ shifter3 0.25 mysubtitles.srt`

Subtitles in mysubtitles.srt show up too late, I want all of them to start 0.25 seconds before:

`$ shifter3 -0.25 mysubtitles.srt`


Subtitles in mysubtitles.srt show up too late, I want all of them to start 1 seconds before AND get the result in a new file named myNEWsubtitles.srt:

`$ shifter3 -1 mysubtitles.srt myNEWsubtitles.srt`

## Installation
