# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("-i", "--ignore-case", action="store_true")


    args = parser.parse_args() # This gets the arguments
    pattern = args.pattern 

    with open(args.filename, 'r') as file:
        lines = file.readlines()

    for line in enumerate(lines):
        line_number = line[0]
        line_words = line[1].rstrip()
        if args.ignore_case:
            if pattern.lower() in line_words.lower():
                print(f"{line_number+1}: {line_words}")
        else:
            if pattern in line_words:
                print(f"{line_number+1}: {line_words}")











if __name__ == "__main__":
    main()
