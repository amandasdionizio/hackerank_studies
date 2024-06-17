#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    contador = 0
    for value in range(a[-1], b[0] + 1):
        if verification_arraymenor(a, value) and verification_arraymaior(b, value):
            contador += 1
    return contador


def verification_arraymenor(vetormenor, value):
    for number_menor in vetormenor:
        if value % number_menor != 0:
            return False
    return True


def verification_arraymaior(vetormaior, value):
    for number_maior in vetormaior:
        if number_maior % value != 0:
            return False
    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
