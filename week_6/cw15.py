s = ["a", "b", "c", "d", "b"]
# 1-method
for i in range(len(s)):
    print(s[i], end=' ')
print()
# 2-method
for x in s:
    print(x, end=" ")
print()
# 3-method
print(*s)