f = open('UGWSCR_After_CFG.txt')
f1 = open('testread1.txt', 'a')
word ='user-profile'

import re
filename = 'UGWSCR_After_CFG.txt'
filename2 = 'testread1.txt'
pattern  = 'user-profile'
new_file = []

# Make sure file gets closed after being iterated
with open(filename, 'r') as f:
   # Read the file contents and generate a list with each line
   lines = f.readlines()

# Iterate each line
for line in lines:
    match = re.findall(r'user-profile .+ \n', line, flags=re.IGNORECASE)
    if match:
        print(match[0])
