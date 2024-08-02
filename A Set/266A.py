number =  input()
color =  input()
remove = 0
for i in range(len(color)):
    if i+1<len(color):
        if color[i+1] == color[i]:
            remove = remove + 1
print(remove)