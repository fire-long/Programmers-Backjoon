import sys
N = int(sys.stdin.readline().strip())

for i in range(1, N+1, 1):
    print(' '*(N-i), end='')
    print('*'*(2*i-1))