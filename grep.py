import sys
import os
import re

def grep(pattern, file_path, invert_match=False, ignore_case=False):
    try:
        with open(file_path, 'r') as file:
            pattern_matched = False
            flags = re.IGNORECASE if ignore_case else 0
            for line in file:
                if (re.search(pattern, line, flags=flags) is not None) != invert_match:
                    print(f"{file_path}:{line}", end='')
                    pattern_matched = True
            return 0 if pattern_matched else 1
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 1

def grep_recursive(pattern, directory, invert_match=False, ignore_case=False):
    exit_code = 1
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            exit_code = max(exit_code, grep(pattern, file_path, invert_match, ignore_case))
    return exit_code

if __name__ == "__main__":
    if len(sys.argv) < 3 or (len(sys.argv) == 3 and sys.argv[1] in ("-r", "-v", "-i")):
        print("Usage: python grep.py [-r] [-v] [-i] <pattern> <file or directory>")
        sys.exit(1)

    recursive = False
    invert_match = False
    ignore_case = False
    i_count = sys.argv[1:].count("-i")
    if i_count > 1:
        print("Only one -i flag allowed.")
        sys.exit(1)
    elif i_count == 1:
        ignore_case = True
        pattern_index = 2
    else:
        pattern_index = 1

    for option in ("-r", "-v"):
        if option in sys.argv[1:]:
            if option == "-r":
                recursive = True
            elif option == "-v":
                invert_match = True

    pattern = sys.argv[pattern_index]
    pattern = pattern.replace('^', r'\A').replace('$', r'\Z')
    path = sys.argv[pattern_index + 1]

    if recursive:
        exit_code = grep_recursive(pattern, path, invert_match, ignore_case)
    else:
        exit_code = grep(pattern, path, invert_match, ignore_case)

    sys.exit(exit_code)
