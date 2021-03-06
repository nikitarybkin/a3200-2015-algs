__author__ = 'Nikita Rybkin'

from sys import stdin, stdout

n = int(stdin.readline())
numbers = map(int, raw_input().strip().split(' '))
numbers.sort()
prev = -1
sticks = []
for i in xrange(len(numbers) - 1, -1, -1):
    num = numbers.pop()
    if num == prev or num == prev - 1:
        sticks.append(num)
        prev = -1
    else:
        prev = num
result = 0
for i in xrange(0, len(sticks) - 1, 2):
    result += sticks[i] * sticks[i + 1]
stdout.write(str(result) + "\n")