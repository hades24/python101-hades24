def payment():
  a=float(input("enter number of hours\n"))
  b=float(input("enter rate per hour\n"))
  if a or b != 0:
    print("payment : ",a*b)
  else:
    return 0

payment()