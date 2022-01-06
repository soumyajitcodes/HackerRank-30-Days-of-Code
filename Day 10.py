#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    inp = bin(n)
    inp = inp[2:]
    print (max(map(len, inp.split('0'))))