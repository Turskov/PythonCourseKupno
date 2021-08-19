print("abc"[0])
print([1, 2][0])
a = 10
b = 20
print([a, b][0])
print([a, b][a < b])  # [a, b][1]

[print(a), print(b)][a < b]  # [None, None][1]
([print, print][a < b])()


