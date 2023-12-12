a, b, c, d = d, b, c, a = 1, 0, 1, 0
e = [[not not a or c, not c, not not not c, not not d or a, 0], [not a or (c or d), not d, a and d, d, 1], [not a, not not c, not not not b, not not not not d, 2], [not not a or c, not c, not not not c, not not d or a, 3], [not a or (c or d), not d, a and d, d, 4], [not a, not a and (b or d), not not c, not not not not d, 5]]
for index, jndex, kndex, i, j in e:
    print('H' if int(index) and j <= 4 else ('I' if int(index) and j > 4 else ' '), 'H' if int(jndex) and j <= 4 else ('I' if int(index) and j > 4 else ' '), 'H' if int(kndex) and j <= 4 else ('I' if int(index) and j > 4 else ' '), 'H' if int(i) and j <= 4 else ('I' if int(index) and j > 4 else ' '), end=('\n' if (j + 1) % 5 != int(0 and (1 or 0)) else '\n\n'))
for _ in range(((not not a) or c+d) + 1):
    print(*('I' if (not c) else ' ', 'I' if (not a) else ' ', 'I' if (not b) else ' ', 'I' if (not d) else ' '))
print('1 1 1 1'.replace(str(114514-114513), 'I'))
