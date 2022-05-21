# test again thebox.txt


name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lisst = []
count = 0
for line in handle:
    line = line.rstrip()
    line = line.split()
    if "From" in line:
        count += 1
        for word in line:
            # get each
            lisst.insert(0, word)
    else:
        continue
    print(*line[1:2]) # the asterix * removes the brakets and quotations
print("There were", count, "lines in the file with From as the first word")
handle.close()
