num = [2, 4, -6, -9, 11, -12, 14, -5, 17]

pos = list(filter(lambda x: x > 0, num))
neg = list(filter(lambda x: x < 0, num))

print(sum(neg))
print(sum(pos))
