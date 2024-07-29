s = input()
lower = 0
upper = 0
for i in range(len(s)):
    if s[i].islower():
        lower = lower + 1
    else:
        upper = upper + 1
if upper > lower:
    print(s.upper())
else:
    print(s.lower())
