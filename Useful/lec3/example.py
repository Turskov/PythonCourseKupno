s = "abcdef"
backup_s = s
print(id(s))
s = s + "g"
print(id(s))
print(id(backup_s))
