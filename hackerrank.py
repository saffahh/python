import math
import os
import random
import re
import sys

def solve(s):
    words=s.split(' ')
    cap_word=[]
    for word in words:
        if word[0].isalpha():
            cap_word.append(word[0].upper()+word[1:])
        else:
            cap_word.append(word)
    return ' '.join(cap_word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
s = input("enter:")
result = solve(s)
fptr.write(result + '\n')
fptr.close()      