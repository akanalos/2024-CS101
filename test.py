def max_value_of_gifts_optimized(n, gifts):
    prefix_sum = {0: -1}  # 前缀和初始化，键为累计和减去520*i，值为索引
    total_sum = 0
    max_value = 0
    cumulative_sum = 0

    for i in range(n):
        cumulative_sum += gifts[i]
        total_sum += 520

        # 计算需要的前缀和差值
        diff = cumulative_sum - total_sum

        # 如果这个差值之前出现过，说明从那个位置到现在这个位置之间的平均值是520
        if diff in prefix_sum:
            current_value = cumulative_sum - (diff + total_sum - 520 * (prefix_sum[diff] + 1))
            max_value = max(max_value, current_value)

        # 如果这个差值没有出现过，记录下来
        if diff not in prefix_sum:
            prefix_sum[diff] = i

    return max_value

# 输入处理
n = int(input().strip())
gifts = list(map(int, input().strip().split()))
# 调用优化后的函数并打印结果
print(max_value_of_gifts_optimized(n, gifts))