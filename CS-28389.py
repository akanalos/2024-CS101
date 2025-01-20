from bisect import bisect_right
from collections import deque


def min_jumps(heights):
    # 用来保存递增子序列的末尾元素
    tails = deque()
    for height in heights:
        # 使用二分查找找到height应该插入的位置
        idx = bisect_right(tails, height)
        if idx == 0:
            # 如果height比所有tails里的元素都小，则添加一个新的测试仪
            tails.appendleft(height)
        else:
            # 否则更新现有的测试仪的高度为更大的height
            tails[idx-1] = height

    # tails的长度即为所需的最小测试仪数量
    return len(tails)


# 示例输入
n = int(input())
heights = list(map(int,input().split()))

# 调用函数并打印结果
print(min_jumps(heights))