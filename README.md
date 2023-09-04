# Python-Scripting
## Shuf.py - Python Implementation of GNU shuf

Consider the old-fashioned Python 2 script [randline.py](https://web.cs.ucla.edu/classes/spring23/cs35L/assign/randline.py)

I used Emacs to write a new script shuf.py in the style of randline.py but using Python 3 instead. My script implements the GNU [shuf](https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html) that is part of GNU Coreutils. GNU shuf is written in C, whereas you want a Python implementation so that you can more easily add new features to it. 


## Features

- Supports the following `shuf` options, with behavior identical to GNU `shuf`:
  - `--echo (-e)`: Display each randomly selected line.
  - `--input-range (-i)`: Treat a range of numbers as input lines.
  - `--head-count (-n)`: Specify the number of output lines.
  - `--repeat (-r)`: Output lines can be repeated.
  - `--help`: Display usage information.

- If `--repeat (-r)` is used without `--head-count (-n)`, the program runs indefinitely, generating random lines indefinitely.

- Supports zero non-option arguments or a single non-option argument "`-`" (to read from standard input) or a single non-option argument specifying an input file name.

## Usage

To use `shuf.py`, follow the format:

```bash
./shuf.py [OPTIONS] [INPUT_FILE]
```

## Example test cases
Shuffle a list of words and display each randomly selected word:
```
./shuf.py -e word1 word2 word3
```
Treat a range of numbers as input and display a specified number of random lines:
```
./shuf.py -i 1-10 -n 5
```
Shuffle lines in a file and display them:
```
./shuf.py file.txt
```
Shuffle lines in a file, display them indefinitely, and repeat the process:
```
./shuf.py -r file.txt
```

## Requirements
This script is written in Python 3 and requires a Python 3 interpreter to run.

It uses the argparse module for command-line argument parsing and the string module for string manipulation.

## Notes
This is a simplified implementation and does not cover all the features of the GNU [shuf](https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html) command. It is designed to meet the specific requirements mentioned in the project description. Feel free to extend and modify it as needed.

