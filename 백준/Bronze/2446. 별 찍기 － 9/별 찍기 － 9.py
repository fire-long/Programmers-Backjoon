import sys
N = int(sys.stdin.readline().strip())
for i in range(1, 2*N, 1):
    if i<=N:
        print(' '*(i-1), end='')
        print('*'*(2*(N-i+1)-1))
    elif i>N:
        print(' '*(2*N-i-1), end='')
        print('*'*(2*(i-N+1)-1))