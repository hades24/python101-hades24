filename="dataset/mbox-short.txt"
try:
  fhand=open(filename)
except: 
  print("FILE NOT FOUND")
num=""
count = 0
for line in fhand:
  line = line.rstrip()
  if line.startswith("X-DSPAM-Confidence:"):
    count = count + 1
    print(count, line)