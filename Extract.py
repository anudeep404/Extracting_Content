#I’m trying to extract a configuration from RSI  file, I’ve written following code, which executes without any error, but fails to create a new file with the extracted content between the patterns. Am I missing something here? 

import re, os
START_PATTERN = '^Last commit$'
END_PATTERN = '^root\@$'
d = raw_input("Enter the file dir: ")
f = raw_input("Enter the file name: ")
os.chdir(d)

with open(f) as file:
    match = False
    newfile = None
    for line in file:
        if re.match(START_PATTERN, line):
            match = True
            newfile = open('rsi_cfg.txt', 'w')
            continue
        elif re.match(END_PATTERN, line):
            match = True
            newfile.close()
            continue
        elif match:
            newfile.write(line)
            newfile.write('\n')
