#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    counter_max = 0
    counter_min = 0
    idx = 0
    max_value = scores[idx]
    min_value = scores[idx]

    while idx < len(scores) - 1:
        if scores[idx + 1] > max_value:
            counter_max += 1
            max_value = scores[idx + 1]
        elif scores[idx + 1] < min_value:
            counter_min += 1
            min_value = scores[idx + 1]
        idx += 1
    return (counter_max, counter_min)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
