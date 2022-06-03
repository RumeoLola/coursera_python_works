# test again thebox.txt


name = input("Enter file: ")
handle = open(name)

lisst = []
for lines in handle:
    lines = lines.rstrip()
    lines = lines.split()
    for word in lines:
        lisst.insert(0, word)

print(*lisst)

handle.close()
