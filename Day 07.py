size = int(input())
number_list = [int(i) for i in input().split()[:size]]
for j in number_list[::-1]:
    print(j, end=' ')