'''

涉及到的题目
LeetCode 20

'''

weight, item_number = 50, 5
dp = [[0 for _ in range(weight + 1)] for _ in range(item_number)]
item_weight, item_value, is_sub = [20,20,10,10,10], [3,3,3,2,1], [5,5,0,0,0]
# for _ in range(item_number):
#     a, b, c = map(int, input().split())
#     item_weight.append(a)
#     item_value.append(b)
#     is_sub.append(c)
zero_index = is_sub.index(0)
for a in range(item_weight[zero_index], weight + 1):
    dp[zero_index][a] = item_weight[zero_index] * item_value[zero_index]

for i in range(item_number):
    for j in range(weight, 10):
        if is_sub[i] == 0:
            if j < item_weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], item_weight[i] * item_value[i] + dp[i][j - item_weight[i]])
for k in range(item_number):
    for l in range(weight, 10):
        if is_sub[k] != 0:
            if l < item_weight[k] + item_weight[is_sub[k] - 1]:
                dp[k][l] = dp[k - 1][l]
            else:
                dp[k][l] = max(dp[k - 1][l],
                               item_weight[k] * item_value[k] + item_weight[is_sub[k] - 1] * item_value[is_sub[k] - 1] +
                               dp[k][l - item_weight[k] - item_weight[is_sub[k] - 1]])
print(dp)
print(dp[-1][-1])