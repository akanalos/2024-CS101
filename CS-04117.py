# pylint: skip-file
import sys
sys.setrecursionlimit(1 << 30)
from functools import lru_cache
dp = [[0] * (51) for _ in range(51)]
dp[0]=[1]*51
for x in range(1,51):
    for y in range(1,51):
        if y==1:
            dp[x][y]=1
        else:
            if x<y:
                dp[x][y]=dp[x][x]
            else:
                dp[x][y]=dp[x][y-1]+dp[x-y][y]
try:
    while True:
        n = int(input())
        print(dp[n][n])
except EOFError:
    pass