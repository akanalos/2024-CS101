def solve(quantities, budget):
    # 定义商品的成本数组
    costs = [1, 2, 5, 10, 20, 50, 100]
    items = []

    # 遍历每个成本和对应的数量
    for cost, quantity in zip(costs, quantities):#将复杂的背包问题拆成0,1背包问题
        count=1
        while quantity>count:
            quantity-=count
            items.append((cost*count,count))
            count = count * 2
        items.append((cost * quantity, quantity))
#items形成了买票的零一背包
    dp=[float('inf')]*(budget+1)
    dp[0]=0
    for item in items:
        for j in range(budget,item[0]-1,-1):
            dp[j]=min(dp[j],dp[j-item[0]]+item[1])
    return dp[budget] if dp[budget] != float("inf") else "Fail"
budget = int(input())
quantities = list(map(int, input().split()))

# 检查预算是否为50的倍数
if budget % 50 != 0:
    print("Fail")
    exit()
budget //= 50
print(solve(quantities, budget))