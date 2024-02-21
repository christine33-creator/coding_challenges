I have been interested in completing the coding challenges from this website: https://codingchallenges.fyi/challenges/challenge-wc

In the first challenge, I write a python script to build a wc tool (more info in the link above).
The python script, if run in a Unix or Windows environment, will support the command line options:
-c (outputs the number of bytes in a file), 
-l (outputs the number of lines in a file), 
-w (outputs the number of words in a file), 
-m (outputs the number of characters in a file), 
and the default option, which is the equivalent to the -c, -l and -w options.

In grep.py challenge, I built my own version of the Unix command line tool grep. Here are what it does:
- implements support for an empty expression
- matches a simple one letter pattern and return the correct exit code to the shell
- recurses a directory tree, that is to support the command line option -r
- implements the -v option. This inverts the search excluding and result that matches
- supports \d and \w in the search pattern. Their meanings are: \d - a digit. \w - a word character.
- implements support for matching ^ match to the beginning of a line and $ matches to the end.

The challenge is from this website: https://codingchallenges.fyi/challenges/challenge-wc
