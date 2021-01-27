a = []
for i in range(1,200):
    if i % 10 == 7:
        a.append(i)
    if i % 7 == 0:
        a.append(i)
    if i // 10 == 7:
        a.append(i)
# print(a)

for b in a:
    if a.count(b)>1:
        for c in range(a.count(b)-1):
            a.remove(b)
print(a)
