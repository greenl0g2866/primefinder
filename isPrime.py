num = input("Enter a number: ")
notPrime = False
if num > 1:
  for i in range(2,num//2):
    if (num%i) == 0:
      notPrime = True
      break
if notPrime == True:
  print(num + "IS NOT a prime number.")
else:
  print(num + "IS a prime number.")
