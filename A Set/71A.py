def shortform(n):
    if len(n)-2 < 9:
        print(n)
    else:
        result = n[0],len(n)-2,n[-1]
        result = "".join(map(str, result))
        print(result)

inp = int(input())
for i in range(inp):
    text = input()
    shortform(text)