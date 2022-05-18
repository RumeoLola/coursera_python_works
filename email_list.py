# test again thebox.txt


name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dice = {}
count = 0
for line in handle:
    line = line.rstrip()
    line = line.split()
    if "From" in line:
        count += 1
        for word in line:
            # get each email
            dice[word] = dice.get(word, 0) + 1
    else:
        continue
    print(line[1:2])
print("There were", count, "lines in the file with From as the first word")
handle.close()
