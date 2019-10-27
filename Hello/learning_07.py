#序列常见方法
a = list("xiaozhao123")
print(a)
b1 = (1, 2, 3, 4, 5, 6)
b2 = list(b1)
print(b2, max(b1), min(b2))
numbers = (1, 2, 3)
print(sum(numbers, 4))
numbers = [1, 100, -29, 66, 86, 32]
numbers = sorted(numbers)
print(numbers)
print(list(reversed(numbers)))