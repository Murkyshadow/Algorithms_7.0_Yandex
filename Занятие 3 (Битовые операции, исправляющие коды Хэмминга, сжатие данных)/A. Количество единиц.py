num = int(input())
two_in_degree = 1
while two_in_degree <= num:
    two_in_degree *= 2
two_in_degree //= 2

count_one = 0
while num > 0:
    if two_in_degree <= num:
        num -= two_in_degree
        count_one += 1
    two_in_degree //= 2

print(count_one)