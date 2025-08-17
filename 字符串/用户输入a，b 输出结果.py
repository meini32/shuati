# map(int, input().split()) 是一种常用的读取并转换输入的方式
# - input() 是 Python 内置函数，作用是读取用户从控制台输入的一行字符串。
# - split() 是字符串的一个方法，作用是按照空白（空格、制表符、换行等）把字符串分割成列表。
# - map() map 把一个函数批量应用到一个序列的每个元素上，得到新的序列,会把列表里的每个元素都应用一次 int 函数，转成整数

'''
示例 1：把字符串数字转成整数
nums = ["1", "2", "3"]
result = map(int, nums)
print(list(result))
# [1, 2, 3]

📌 示例 2：把所有字符串变成大写
words = ["hello", "python", "map"]
result = map(str.upper, words)
print(list(result))
# ['HELLO', 'PYTHON', 'MAP']

📌 示例 3：用自定义函数
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
result = map(square, numbers)
print(list(result))
# [1, 4, 9, 16]
'''

a,b = map(int,input().split())
def add(a, b):
    return a + b

print(add(a,b))