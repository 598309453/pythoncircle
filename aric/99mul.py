# 打印99乘法表
'''
1. 首先实现
1*1=1
print(1, "*", 1, "=", 1)

连接用逗号，一些非数字符号用引号引起来

 2. 实现
1*1=1
1*2=2
for i in range(1, 3):
    result= 1*i
    print(1, "*", i, "=", result)

3. 实现
1*1=1
1*2=2  2*2=4
1*3=3  2*3=6  3*3=9
......

\t : 横向制表符, 使格式对齐
end="": 说明打印后跟空格，即下一个打印接着后面输出。默认是换行，会在下一行输出下一个内容
print(""): 表示换行
'''

# for i in range(1, 10):
#     for j in range(1, i+1):
#         result = j * i
#         print(j, "*", i, "=", result, "\t", end="   ")
#     print("")

