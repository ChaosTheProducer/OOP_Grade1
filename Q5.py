# Q5
str1 = input('Please input a string here: ')

isPalidrome = True  # 设置一个Flag，默认是对的，除非我们可以反证它

for i in range(0, len(str1) // 2):
    if str1[i] != str1[len(str1) - i - 1]:
        isPalidrome = False

if isPalidrome:
    print(str1, 'is a palidrome.')
else:
    print(str1, 'is not a palidrome')
