# -*- coding: utf-8 -*-

#print("1024 * 768=",1024 * 768)

# a=100
# if a>0:
#     print(a)
# else:
#     print(-a)

# a="xyz"
# b=a
# a="789"
# print(b);
# print(a);
#
# print(10/3);    #正常的除法
# print(10//3);   #取模
# print(10%3);    #取余
#
# print('\'m');   #转义
# print(r'\\\t');   #转义

print(len('abcdf'));   #字符长度

##你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，
# %s表示用字符串替换，
# %d表示用整数替换，
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
# 如果只有一个%?，括号可以省略。
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

#list
mirical=['zhangshan','lisi','wangwu']
print(mirical)
#用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(mirical[0])
#list添加元素
mirical.append('english')
print(mirical)
#可以把元素插入到指定的位置，比如索引号为1的位置：
mirical.insert(2,'chinese')
print(mirical)
#删除list元素
mirical.pop(1)
print(mirical)

###元组##另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就【不能修改】，比如同样是列出同学的名字
simple=(1,2,3)
print(simple)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])

#条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# •低于18.5：过轻
# •18.5-25：正常
# •25-28：过重
# •28-32：肥胖
# •高于32：严重肥胖

h=1.75
f=80.5
bmi=h*100/f
if bmi>32:
    print('高于32：严重肥胖')
elif bmi>28:
    print('28-32：肥胖')
elif bmi>25:
    print('25-28：过重')
elif bmi>18.5:
    print('18.5-25：正常')
else:
    print('低于18.5：过轻')