# 冒泡排序法
# 要实现多趟比较，可以在一趟比较的循环外再加上一个for循环

lis = list(input("请输入一串数字："))
lens = len(lis)
for j in range(0, lens):
    for i in range(0, lens - 1):
        if lis[i] > lis[i + 1]:
            tmp = lis[i]
            lis[i] = lis[i + 1]
            lis[i + 1] = tmp
print("你所输入的数字从小到大的顺序为：", lis)

