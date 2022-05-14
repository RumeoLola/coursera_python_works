# test again thebox.txt


name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# declare empty dictionary
dice = dict()
largest = 0

for line in handle:
    line = line.rstrip()
    line = line.split()
    for word in line:
        dice[word] = dice.get(word, 0) + 1
        # here I pass two parameters to the following for loop
        for word, count in dice.items():
            if count > largest:
                largest = count
print("The most common word is", word, "with a total count of", largest)
handle.close()
