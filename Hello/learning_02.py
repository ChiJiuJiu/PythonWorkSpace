# 循环
word = "xiaozhao"
for i in word:
    print(i, end=" ")
print('\n')
member = [1, 2, 3, "123", '312']
for i in member:
    print(type(i), len(member), end=' ')

print('\n')
# range()函数
number = range(1, 10, 2)
for i in number:
    print(i, end=' ')
print('\n')
number = list(range(5))
print(number, end='\n')

for i in range(5):
    print("this is ", i)

bingo = "123"
answer=input('intput a number\n')
while True:
    if answer == bingo:
        break
    answer = input('incorrect, input again\n')
print("correct")

