n = int(input())  

suitcases = []
for _ in range(n):
    x, y, z = map(int, input().split())
    suitcases.append((x, y, z))

suitcases.sort()

count = 0

for i in range(n):
    current_suitcase = suitcases[i]
    for j in range(i):
        if suitcases[j][0] < current_suitcase[0] and suitcases[j][1] < current_suitcase[1] and suitcases[j][2] < current_suitcase[2]:
            count = max(count, dp[j])
    count += 1

print(count)
