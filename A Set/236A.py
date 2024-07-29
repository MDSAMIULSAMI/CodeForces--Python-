a = input()
uniqe = []
for i in range(len(a)): 
    if a[i] not in uniqe: uniqe.append(a[i])
if len("".join(uniqe)) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")