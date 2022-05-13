filename="dataset/mbox-short.txt"
fhand=open(filename)
num=""
for line in fhand:
  if line.startswith("X-DSPAM-Confidence:"):
    print(line)