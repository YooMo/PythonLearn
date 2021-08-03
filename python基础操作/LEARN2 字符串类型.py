# PYTHON的数据类型

# 常见的数据类型
# 1.字符串类型
love = "i love u"
like = "你真棒"
helloworld = "你好 世界!"
print(love, helloworld, like)
# 大字符串可以换行，也很帅，也是str类型
# 大字符串还可以当注释使用（当你没有把此字符串赋值给某一变量时）
s = '''
这是一个大字符串
我用s来接收了
绿色的好看是这样的
'''
print(s, type(s))
# 在python中，type()用于返回数据类型
# <class 'str'>字符串类型
print(love, type(love))

# # 单双引号可以互相嵌套
# s = 'i love u'
# s = 'i "love" u ' 此情况可以嵌套 打印出来的效果是带着引号的


# # 关于转义字符 在字符串内使用
# \n 换行
# \t 制表符
c = 'yoom\no\n'
d = r'yoo\nmo\n'  # 在字符串前加r可以去除转义字符效果
e = 'wo\\wp'
print(c, d, e)
