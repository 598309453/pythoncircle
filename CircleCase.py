# for 循环语句学习
# 注意点：
# 1. 每个循环后面要写冒号
# 2. 要注意缩进格式
# 3. 注意步长，默认为1
# 4. 如果步长为负数，则范围是先写大的数，再写小的数
# 5. range 的范围是左闭右开
'''
# 默认自增长为 1
for i in range(1, 6):
    print("i=", i)
-----------------------------
# 步长为指定的值
for i in range(1, 6, 2):
    print("i=", i)
-----------------------------
s = 0
for i in range(1, 6):
    s = s + i
    print("s=", s)
=>
s= 1
s= 3
s= 6
s= 10
s= 15
------------------------------

for i in range(6, 1, -2):
    print('i=', i)
=>
i= 6
i= 4
i= 2

'''

'''
# 双重for循环
for i in range(1, 4):
    for j in range(1,3):
        print("i=", i, "j=", j)
=>
i= 1 j= 1
i= 1 j= 2
i= 2 j= 1
i= 2 j= 2
i= 3 j= 1
i= 3 j= 2

-----------------------------------
for i in range(1, 4):
    for j in range(1, i+1):
        print("i=", i, "j=", j)
=>
i= 1 j= 1
i= 2 j= 1
i= 2 j= 2
i= 3 j= 1
i= 3 j= 2
i= 3 j= 3
 
'''
