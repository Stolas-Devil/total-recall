import math
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

A, B, C = [int(i) for i in input().split()]

L, H = [int(i) for i in input().split()]

sq = (A * C + B * C) * 2 + A * B

fill_sq = sq * 0,85 * 1,1

print(math.ceil(fill_sq / ((L * H) / 1000000)))


