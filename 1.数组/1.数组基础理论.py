'''
数组基础理论
'''
'''
数组理论基础
数组是存储在连续内存空间上的相同类型数据的集合，有两个特征
    1.数组下标都是从0开始（顺向）；或者从-1开始（逆向）
    2.数组在内存空间的地址是连续的
    3.由于增添或者删除元素都要对后面的元素地址做移动，所以数组中的元素不能删除，只能覆盖
'''

arr = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(arr)):
    print(id(arr[i]), end=', ')

# 2055794262256, 2055794262288, 2055794262320, 2055794262352, 2055794262384, 2055794262416, 2055794262448,
# 可以看出由于元素的类型是整数型int，整数型每个元素占4个字节，所以id是四个一增加
