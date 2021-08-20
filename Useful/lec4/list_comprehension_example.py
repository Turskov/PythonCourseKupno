

lst = []
for i in range(11):
    if i % 2 == 0:
        lst.append(i)

lst2 = [i if i % 2 == 0 else "*" for i in range(11)]

# i = 0
# while i <= 10:
#     if i % 2 == 0:
#         lst.append(i)
#     i += 1

print(lst)
print(lst2)
