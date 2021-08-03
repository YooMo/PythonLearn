# 基础数据类型转换

# 转换的模式 : 1.自动类型转换 2.强制类型转换


# # 自动类型转换
# #first
# print(123 + True)   # 此时bool值转化为int值进入计算中，True代表1，False代表0
#
# #second
# print(12.5 + 99)
#
# #last
# print(True + 3.1415)
# True ==> 整型 ==> 浮点 ==> 复数

# 强制类型转换
'''
str()
int()
float()
bool()
list()
tuple()
set()
dict()
etc...
使用以上方法可以转化数据类型(得是靠谱的才能转化 你要真想字符串转int那我只能哈哈）

int(x [,base])

将x转换为一个整数

long(x [,base] )

将x转换为一个长整数

float(x)

将x转换到一个浮点数

complex(real [,imag])

创建一个复数

str(x)

将对象 x 转换为字符串

repr(x)

将对象 x 转换为表达式字符串

eval(str)

用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)

将序列 s 转换为一个元组

list(s)

将序列 s 转换为一个列表

set(s)

转换为可变集合

dict(d)

创建一个字典。d 必须是一个序列 (key,value)元组。
'''
