text = input()
text = text.lower()
store = []
for i in text:
    if i.startswith("a") or i.startswith("e") or i.startswith("i") or i.startswith("o") or i.startswith("u") or i.startswith("y"):
        i = ""
    else:
        # print("."+i)
        store.append("."+i)
        # print(x)
x = "".join(store)
print(x)