# test again thebox.txt


name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dice = dict()
for line in handle:
    line = line.rstrip()
    line = line.split()
    for word in line:
        dice[word] = dice.get(word, 0) + 1
        print(word, dice[word])
handle.close()
