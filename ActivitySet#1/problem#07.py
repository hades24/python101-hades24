text = "X-DSPAM-Confidence:    0.8475"
num  = ""
for a in text:
  if a.isdigit():
    num = num + a
x=float(num)
print(x) 