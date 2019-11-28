# 折半查找

a = 90
lis = [1, 5, 7, 9, 12, 23, 90]
lens = len(lis)
left = 0
right = lens-1
mid = (left+right)//2
while left <= right:
    if a > lis[mid]:
        left = mid+1
    elif a < lis[mid]:
        right = mid-1
    else:
        print("a是列表中的第", mid+1, "个数")
        break
    mid = (left+right)//2   # 这一步是给mid再次定义，循环外的定义在第二次循环后不起作用
if left > right:
    print("没有找到")

