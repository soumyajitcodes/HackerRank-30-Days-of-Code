"""
Given a string, S, of length  N that is indexed from 0 to N - 1,
print its even-indexed and odd-indexed characters as 2 space-separated strings
on a single line.
Note: 0 is considered to be an even index.
"""
test_cases = int(input())
while test_cases:
    string = input()
    temp = []
    temp1 = []
    for i in range(len(string)):
        if i % 2 == 0:
            temp.append(string[i])
        else:
            temp1.append(string[i])
    a = ''
    b = ''
    a = a.join(temp)
    b = b.join(temp1)
    print(f'{a} {b}')
    # for j in temp:
    #     print(j, end='')
    # for k in temp1:
    #     print(k, end='')
    test_cases -= 1