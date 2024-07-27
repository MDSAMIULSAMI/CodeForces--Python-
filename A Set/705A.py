n = int(input())

hate_text = "I hate"
love_text = "I love"
result = []

for i in range(n):
    if int(i)%2 != 0:
        result.append(love_text)
        result.append("that")
    if int(i)%2 == 0:
        result.append(hate_text)
        result.append("that")

result.pop(-1)
result.append("it")
x =" ".join(result)
print(x)