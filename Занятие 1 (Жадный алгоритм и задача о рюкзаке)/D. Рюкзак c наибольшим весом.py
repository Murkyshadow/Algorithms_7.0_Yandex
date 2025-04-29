# с помощью рюкзака находим наибольшую массу
n, size = map(int,input().split())
weights = list(map(int, input().split()))
all_sizes = [-1] * (size+1)
all_sizes[0] = True
max_size = 0
for w in weights:
    for i in range(size-w, 0-1, -1):
        if all_sizes[i] != -1:
            all_sizes[i+w] = True
            max_size = max(max_size, i+w)
print(max_size)