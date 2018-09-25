#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
import sys  # 导入sys.py
import math  # 导入math库
import time
import calendar
import datetime
import os
print(sys.argv)  # 输出路径


def main():
    str1 = 'h' \
              'e' \
              'y'
    str2 = "a" \
           "s" \
           "d"
    str3 = '''c
       c
       c'''
    a = b = c = 1  # 创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
    d, e, f = 3, 4, 'fff'
    a1 = 'a b c d e'
    print(a1[1:4])  # 空格b空格
    print(a1[3])  # 3号索引
    print(a1[-5:-1])  # 从倒五至倒一
    print(a1[-1:])  # 从倒一开始
    print(a1[2:])  # 从2号索引开始 (包前不包后)b c d e
    print(a1[:2])  # 2号索引之前的所有
    print(a1 * 2)  # 输出2遍
    print(a1 + " f g")
    print(str1)
    print(str1+'\n')
    print(str2)
    print(str3)  # print输出默认另起一行
    print(str1, str2)  # 同行内输出2个变量
    #  列表
    list1 = ['zz','xx','cc',1,2,3]
    list2 = list1[1:2]
    #  元组
    tuple1 = ('zz','xx','cc',1,2,3)  # tuple元组相当于只读的列表 不可二次赋值
    print(list2)
    print(list1 + list2)
    # print(list1 + a)  # 列表只能连接列表
    print(tuple1)
    #  字典
    dict1 = {}  # 字典是无序的
    dict1['sex'] = 'male'
    dict1 = {'name': '张三', 'age': 30}
    print(dict1)  # {'name': '张三', 'age': 30}
    print(dict1.keys())
    print(dict1.values())
    # 类型转换
    # str(a)
    # int()
    # chr()
    # tuple()
    # dict()
    # 运算符
    print(9.0 // 2)  # 4.0 向下取整
    print(5 ** 3)  # 125 幂运算
    # print(a != b)  # False
    '''
    type()
    不会认为子类是一种父类类型。
    isinstance()
    会认为子类是一种父类类型。
    '''
    #  逻辑符
    a, b, c, d = False, 10, 20, 0  # False和0都是False
    print(a and b)  # and:False/0或后者
    print(b and c)
    print(c and b)
    print(b and d)
    print(a and d)
    print(d and a)
    print(d and b)
    print(a or b)  # or:输出前者；当前者为False/0时，结果为后者
    print(c or b)
    print(b or d)
    print(a or d)
    print(d or a)
    print(d or b)
    print(d or a)
    print(not d)  # True
    # 身份运算符
    '''
    is 与 == 区别： 交互模式和脚本模式结果不同
    is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
    >> > a = [1, 2, 3]
    >> > b = a
    >> > b is a
    True
    >> > b == a
    True
    >> > b = a[:] 会生成新的对象
    >> > b is a
    False
    >> > b == a
    True
    '''
    # a= 1
    # sum1 = 0
    # while a==1:
    #     num =int(input("输入一个数"))
    #     sum1 += num
    #     print(sum1)
    # for循环
    str1 = 'qwerty'
    for i in str1:
        print(i)
    fruits = ['apple', 'banana', 'orange']
    for i in range(len(fruits)):
        print(fruits[i])
    print("bye!")
    # 质数
    # sum,list1 =0, []
    # for num in range(10, 30):
    #     num += 1
    #
    #     for i in range(2, num):
    #         if num % 2 == 0:
    #             break
    #     else:
    #         sum+=num
    #
    #         list1.append(num)
    #         print(list1,sum)

    for num in range(10,20):   # 迭代 10 到 20 之间的数字
        for i in range(2,num):  # 若整除则break跳出i循环；若不整除则不进入if嵌套，直接进行range,
                                # 直到num=13，i=12时,range(2,13)已放不了13，进入else)
            if num % i == 0:      # 确定第一个因子
                j = num/i          # 计算第二个因子
                # print('%d 等于 %d * %d' % (num,i,j))
                break            # 跳出当前i循环 num+1
        else:                  # 和i循环并列，else表示for循环为False时执行，即 i不在(2,num),即i==num时
            print(num, '是一个质数')


    # 100以内质数
    arr1,i= [],2
    for i in range(2,100):
        j =2
        for j in range(2,i):
            if i%j ==0: break;
        else:
            arr1.append(i)
    print(arr1)
    # continue 用于过滤不要的元素
    n = 0
    while n <10:
        n += 1
        if n%2==0:
            continue
        print(n)

    print('\n')  # 输出换行
    print(r'\n')  # 字面意思输出字符串 ''中的内容
    print("My name is %s,I'm %d years old" % ('张三',30))

    arr1 =[1,'2',3,'a',4,6,'a']
    var2 =[34,5,7]
    print([1,2,3]+['zz',2,3])
    print(arr1.index('a'))  # 获取arr1的第一个‘a’的索引值

    temp = (1,2,3,4)
    temp = (1,2,3,3,4)
    print('1234',temp)
    dict1 ={'a':'aaa','b':'bbb','c':'ccc'}
    print(dict1['a'])
    print(str(dict1))
    print(type(dict1))
    dict1.clear()  # 清空该字典所有条目
    del dict1  # 删除该字典 有别于del()

    ticks =time.time()
    print("当前时间戳为",ticks)
    localtime1=time.localtime(ticks)
    localtime2=time.asctime(localtime1)
    print(localtime1)
    print('格式化时间',localtime2)
    # 格式化日期
    print(time.strftime("%Y-%m-%d %H:%M:%S %a %b %d",time.localtime()))
    # 获取日历
    cal=calendar.month(2018,9)
    print(cal)
    # print(time.clock())

    i = datetime.datetime.now()
    print("当前的日期和时间是 %s" % i)
    print("ISO格式的日期和时间是 %s" % i.isoformat())
    print("当前的年份是 %s" % i.year)
    print("当前的月份是 %s" % i.month)
    print("当前的日期是  %s" % i.day)
    print("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
    print("当前小时是 %s" % i.hour)
    print("当前分钟是 %s" % i.minute)
    print("当前秒是  %s" % i.second)

    # 创建函数
    def hello(words):  # 1个形参
        print(words)
    hello("qwerqwrqw")
    hello(words='hello lolo')  # 关键字参数
    def changeInt(a):
        "传不可变对象numbers、strings、tuples"
        a = 10
    b= 2
    changeInt(b)
    print(b)

    def changeList(myList):
        "传递可改变对象list、dictionary"
        myList.append(['a','b',1])
    list2=[1,2]
    changeList(list2)
    print(list2)

    def printInfo(age,name='miki'):  # 省缺值
        print("age=",age)
        print("name=",name)
    printInfo(30,)
    printInfo(age=35,name='mike2')

    # 不定长参数
    def printInfo2(arg1,*allInfo):
        "打印所有参数"
        print(arg1)
        for i in allInfo:
            print(i)

    printInfo2(1,2,3,4,4,5,6,4,3,'zz')

    # 匿名函数表达式lambda 不能访问外部变量
    sum2 = lambda arg1,arg2:arg1+arg2
    print(sum2(20,30))
    # 可在函数内用global修饰声明全局变量 python假设任何在函数内赋值的变量都是局部的
    # money=2000
    # def getMoney():
    #     global money  # 没有就认为没有声明和初始化局部变量
    #     money=money+1000
    #     print(globals())
    # print(money)
    # getMoney()
    # print(money)

    # dir() 返回一个模块里定义过的名字
    contant1=dir(math)
    print(contant1)

    # 导入包 调试
    from package_runoob.runoob1 import runoob1
    from package_runoob.runoob2 import runoob2

    runoob1()
    runoob2()

    fo =open(r'D:\fo.txt','w+')
    fo.write("www.runoob.com")
    fo.close()
    #
    fo = open(r'D:\fo.txt', 'w+')
    str2=fo.read(5)
    print(str2)

    # 异常
    try:
        fh = open("testfile", "w")
        try:
            fh.write("这是一个测试文件，用于测试异常!!")
        finally:
            print("关闭文件")
            fh.close()
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        print("内容写入文件成功")
        fh.close()

    # 类
    class Test:
        def prtt(self):
            print(self)  # self代表类的事例 代表地址
            print(self.__class__)  # 指向类
    t= Test()
    t.prtt()
    # 创建类
    class Employee:
        '所有员工的基类'
        empCount=0
        def __init__(self,age,salary):
            self.age=age
            self.salary=salary
            Employee.empCount +=1
        def getCount(self):
            print('员工数量为',Employee.empCount)
        def getInfo(self):
            print('员工信息',self.age,'员工薪资',self.salary)
        # 销毁 垃圾回收
        def __del__(self):
            class_name = self.__class__.__name__
            print(class_name, "销毁")

    # 创建实例化对象
    emp1 =Employee(28,9999)
    emp2 =Employee(30,99999)
    print(Employee.empCount)
    emp1.getCount()
    emp2.getInfo()
    emp1.name='www'
    # 类的内置类
    print(Employee.__doc__)
    print(Employee.__dict__)

    # 访问私有变量
    class Runoob:
        __site = "www.runoob.com"  # 双下划为私有变量 单下划为protected型变量

    runoob = Runoob()
    print(runoob._Runoob__site)  # 对象名._类名__私有属性名 访问私有属性，直接对象.属性会报错

    import re  # 导入正则表达式
    # match:在开头处匹配，匹配不到则none
    print(re.match('www','www.baidu.com'))  # span(0,3) match= 'www'
    print(re.match('com','www.qq.com'))  # none
    # search:匹配整个字符串，直到找到一个匹配。
    info1 ="Cats are smarter than dogs"
    searchObj=re.search(r'(.*) are (.*?) .*', info1, re.M|re.I)
    '''        r ''  字符本意'' 
     (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
     (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
        后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
     re.M  :匹配多行  re.I:忽视大小写
    '''
    if searchObj:
       print ("searchObj.group() : ", searchObj.group())
       print ("searchObj.group(1) : ", searchObj.group(1))
       print ("searchObj.group(2) : ", searchObj.group(2))
    else:
       print ("Nothing found!!")
    # re.sub(pattern,repl,string,count)
    #       (正则选取,替换为(可为函数),原始对象,替换次数(默认0为所有))
    phone = "2004-959-559 # 这是一个国外电话号码"
    # 删除字符串中的 Python注释
    num = re.sub(r'#.*$', "", phone)
    print("电话号码是: ", num)  # 2004-959-559
    # 删除非数字(-)的字符串  # 2004959559
    num = re.sub(r'\D', "", phone)
    print("电话号码是 : ", num)




if __name__ == '__main__':
    main()  # 在脚本最后调用主函数main()，表示只有直接运行时会执行该main() import不会运行，常用于测试代码安放
