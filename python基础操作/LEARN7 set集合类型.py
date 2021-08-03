#set集合类型

'''
set类型是无序且不重复的数据类型
使用大括号来声明
'''

vars = {1,2,3,'a','b'}
print(vars)

vars1 = set('123456')
print(vars1)
'''
如果需要定义空集合只能用set（）函数而不能用 = {}
因为后者定义的是空字典
'''
vars2 = {}
vars3 = set()
print(type(vars2),type(vars3))

'''
向集合添加内容
'''

a = {1,2,3}
a.add('a')
print(a)

'''
向集合删除内容、检测内容是否在内
'''
a.discard(a)
print(a)


"""
对集合后续的操作太多 跳过了
a.pop()
a.discard()
a.difference()
etc..
需要时可以使用文档查询
"""