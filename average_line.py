# test against thebox.txt
file_name = input("Enter file name: ")
hand_file = open(file_name)

count, tot_num = 0, 0

for line in hand_file:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        tot_num += float(line.split()[1])
    else:
        continue
print("Average spam confidence:", float(tot_num)/count)

hand_file.close()
