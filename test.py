"""
    字符串拼接
"""
# radius_ = float(input("Enter radius: "))
# perimeter = 2 * 3.1416 * radius_
# area = 3.1416 * radius_ * radius_
# print("周长: %.2f" % perimeter)
# print("Area: %.2f" % area)
# """
#     身份验证
# """
# username = input("Enter username: ")
# password = input("Enter password: ")
# if username == "admin" and password == "123456":
#     print("Login success!")
# else:
#     print("Login failed!")

"""
    分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)    
"""
# x = float(input("x = "))
# if x > 1:
#     y = 3 * x - 5
# elif x < -1:
#     y = 5 * x + 3
# else:
#     y = x + 2
# print("f(%.2f) = %.2f" % (x, y))

"""
        分段函数求值进阶
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)    
"""
# x = float(input("x = "))
# if x > 1:
#     y = 3 * x - 5
# else:
#     if x >= -1:
#         y = x + 2
#     else:
#         y = 5 * x + 3
# print("f(%.2f) = %.2f" % (x, y))

"""
    英制单位英寸与公制单位厘米互换
"""
# value = float(input("请输入长度: "))
# unit = input("请输入单位: ")
# if unit == 'in' or unit == '英寸':
#     print('%.2f英寸 = %.2f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%.2f厘米 = %.2f英寸' % (value, value / 2.54))
# else:
#     print("请输入有效的单位")

"""
    百分制成绩转换为等级制成绩。
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
"""
# score = float(input("请输入成绩: "))
# if score >= 90:
#     print("A")
# elif 80 <= score < 90:
#     print("B")
# elif 70 <= score < 80:
#     print("C")
# elif 60 <= score < 70:
#     print("D")
# else:
#     print("E")

"""
    判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
    构成三角形的条件是:任意两边之和必须大于第三边。
    已知三边（海伦公式）:
    公式: S = √[s(s-a)(s-b)(s-c)]
    解释: 其中 s = (a+b+c)/2，表示半周长。这个公式在已知三边的情况下，可以直接计算面积。
"""
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a + b > c and a + c > b or a + c > b:
#     print('三角形周长是 %.2f' % (a + b + c))
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print('面积: %.3f' % area)
# else:
#     print('不能构成三角形')
"""
    用for循环实现1~100求和
"""
# sum = 0
# for x in range(101):
#     sum += x
# print(sum)
"""
    用for循环实现1~100之间的偶数求和
"""
# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)

"""
    猜数字游戏
"""
# import random
#
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     if counter > 7:
#         print('你的7次已经用完了')
#         break
#     guess = int(input('请输入: '))
#     if guess == answer:
#         print('恭喜你猜对了!')
#         print('你总共猜了%d次' % counter)
#         break
#     else:
#         if guess > answer:
#             print('大了')
#         else:
#             print('小了')
#         counter += 1

"""
    输出乘法口诀表(九九表)
"""
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

"""
    输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数。
"""
# from math import sqrt
#
# num = int(input("请输入一个整数: "))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print("%d是素数" % num)
# else:
#     print("%d不是素数" % num)

"""
    埃拉托斯特尼筛法，找出小于等于n的所有素数
"""
# 创建一个长度为n+1的列表，初始值都为True，表示都是素数
# 找出小于等于100的所有素数
# n = 100
# primes = [True] * (n + 1)
# primes[0] = primes[1] = False  # 0和1不是素数
#
# # 从2开始，遍历到sqrt(n)
# for i in range(2, int(n ** 0.5) + 1):
#     if primes[i]:
#         # 如果i是素数，则将i的倍数标记为合数
#         for j in range(i * i, n + 1, i):
#             primes[j] = False
#
# # 返回所有素数的索引
# print([i for i in range(2, n + 1) if primes[i]])

"""
    输入两个正整数计算它们的最大公约数和最小公倍数
    提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数
"""
# x = int(input('x = '))
# y = int(input('y = '))
# # 如果x大于y就交换x和y的值
# if x > y:
#     # 通过下面的操作将y的值赋给x, 将x的值赋给y
#     x, y = y, x
# # 从两个数中较小的数开始做递减的循环
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break
"""
    寻找水仙花数。
    说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
"""
# for num in range(100,1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low**3 + mid**3 + high**3:
#         print(num)
"""
    正整数的反转
    我们通过整除和求模运算分别找出了一个三位数的个位、十位和百位，这种小技巧在实际开发中还是常用的。用类似的方法，我们还可以实现将一个正整数反转，例如：将12345变成54321，代码如下所示。
"""
# num = int(input("请输入一个整数: "))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)
"""
    百钱百鸡问题。
    公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只.' % (x, y, z))
"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，
如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
"""

# from random import randint
#
# money = 1000
# while money > 0:
#     print('你的总资产为:', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了, 游戏结束!')

"""
    生成斐波那契数列的前20个数。
"""
# def fibonacci_generator(n):
#     """
#     使用生成器表达式生成斐波那契数列
#
#     Args:
#       n: 生成数列的长度
#
#     Yields:
#       int: 斐波那契数
#     """
#
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# # 生成前20个斐波那契数列
# result = list(fibonacci_generator(20))
# print(result)
#
#
# def fibonacci_iterative(n):
#     """
#     使用循环迭代生成斐波那契数列
#
#     Args:
#       n: 生成数列的长度
#
#     Returns:
#       list: 斐波那契数列的前n个数
#     """
#
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[i - 1] + fib[i - 2])
#     return fib
#
#
# # 生成前20个斐波那契数列
# result = fibonacci_iterative(20)
# print(result)
"""
    输出100以内所有的素数。
    素数指的是只能被1和自身整除的正整数（不包括1）。
"""
# from math import sqrt
#
# primeNumbers = []
# for num in range(0, 101):
#     end = int(sqrt(num))
#     is_prime = True
#     for x in range(2, end + 1):
#         if num % x == 0:
#             is_prime = False
#             break
#     if is_prime and num != 1:
#         primeNumbers.append(num)
# print(primeNumbers)
# print('python is good language'.title())
# name='zhang san'.title()
# date='2024-05-04'
# print(f'{name}您好,今天是{date}')

# def city_country(city,country):
#     return f"{city}, {country}"
#
# print(city_country('深圳','中国'))
# print(city_country('上海','中国'))
# print(city_country('北京','中国'))

"""
    面向对象编程
"""

# class CuteCat:
#     def __init__(self,cat_name,cat_color,cat_weight):
#         self.name = cat_name
#         self.color = cat_color
#         self.weight = cat_weight
#
#     @staticmethod
#     def speak():
#         print('喵喵喵')
#
# cat = CuteCat('mili','白色','5.6')
# print(cat.name)
# print(cat.color)
# print(cat.weight)
# cat.speak()
"""
    对象继承
"""
# class Mammal:
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#
#     def breathe(self):
#         print(self.name + '在呼吸')
#
#     def poop(self):
#         print(self.name + '在拉屎')
#
# class Human(Mammal):
#     def __init__(self, name, sex, age):
#         super().__init__(name, sex)
#         self.age = age
#
#     def eat(self):
#         print(self.name + '在吃东西')
#
#     def sleep(self):
#         print(self.name + '在睡觉')
#
# class Cat(Mammal):
#     def __init__(self, name, sex, color):
#         super().__init__(name, sex)
#         self.color = color
#
#     def eat(self):
#         print(self.name + '在吃鱼')
#
#     def sleep(self):
#         print(self.name + '在睡觉')
#
#
# cat = Cat('mili', '公', '白色')
# cat.poop()
# cat.eat()
# cat.sleep()

"""
    读写文件
"""
# from pathlib import Path
# path = Path('/home/zbl/a.key')
# # 读文件
# content = path.read_text(encoding='utf-8')
# print(content)
# lines = content.splitlines()
# for line in lines:
#     print(line)
# # 写文件
# path.write_text('hello world', encoding='utf-8')
"""
    写文件作业
"""
# from pathlib import Path
#
# names = ''
# user_input = input("请输入访客名字(完成所有名字输入后,请输入q终止程序):")
# while user_input != 'q':
#     names += user_input + '\n'
#     user_input = input("请输入访客名字(完成所有名字输入后,请输入q终止程序):")
#
# path = Path('/home/zbl/访客名单.txt')
# path.write_text(names, encoding='utf-8')
"""
    try except 异常捕获
"""
# try:
#     print(1 / 1)
# except ZeroDivisionError:
#     print('除数不能为0')
# else:
#     print('没有发生异常')
# finally:
#     print('无论是否发生异常，都会执行')
"""
    异常捕获作业两个数字相加
"""
# a = input('请输入第一个数字:')
# b = input('请输入第二个数字:')
# try:
#     result = int(a) + int(b)
# except ValueError:
#     print('发生异常请输入数字')
# else:
#     print(result)
# finally:
#     print('运行结束')
"""
    断言 assert  测试用例 ,以test_开头即可 pytest测试库
"""
# def my_adder(x,y):
#     return x+y
#
# def test_positive_with_positive():
#     assert my_adder(1,2) == 3

"""
    fixture 装饰器
"""


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount

