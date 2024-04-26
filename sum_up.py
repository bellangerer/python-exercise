while True:
  n1 = int(input("Enter a number: "))
  if n1 < 0:
    print("n1 needs to be >= 0")
    continue

  n2 = int(input("Enter a 2nd number: "))
  if n2 < 0:
    print("n2 needs to be >= 0")

  if n2 <= n1:
    print("n2 needs to be > n1")
    continue

  for i in range(n1,n2):
      print(i , end="")
  print()
