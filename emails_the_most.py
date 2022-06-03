# test again thebox.txt


name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = 0
dice = {}
for lines in handle:
    lines = lines.rstrip()
    lines = lines.split()
    if "From" in lines:
        for word in lines:
            word = lines[1]
            dice[word] = dice.get(word, 0) + 1
            for word, iter in dice.items():
                if iter > count:
                    word = word
                    count = iter
    else:
        continue
print(word, count)

handle.close()
