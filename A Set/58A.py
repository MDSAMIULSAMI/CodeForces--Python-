import re
text = input()

pattern = r'h.*?e.*?l.*?l.*?o'
search = re.search(pattern,text)

if search:
    print("YES")
else:
    print("NO")