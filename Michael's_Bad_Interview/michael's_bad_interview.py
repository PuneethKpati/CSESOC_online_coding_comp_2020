#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'bad_interview' function below.
#
# The function accepts INTEGER n as parameter.
#

def bad_interview(n):
    # Write your code here
    for x in range(1,n+1):
        if x % 4 == 0 and x % 6 == 0:
            print("CSESocRocks")
            continue
        elif x % 4 == 0:
            print("CSESoc")
            continue
        elif x % 6 == 0:
            print("Rocks")
            continue
        else:
            print(x)
        
        
if __name__ == '__main__':
    num = int(raw_input().strip())

    bad_interview(num)
