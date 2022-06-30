# primefinder
Python program which takes and input and checks if it is a prime number.

A method to find out if a number is prime is to take the number (num) and divide it by 2 all the way to num//2.
If num is divisible by even one number, it is not a prime number.

The program first checks if num is positive.
It then checks if there is a remainder when divided with numbers from 2 to n//2.
The program will then loop, and if it detects num%i == 0 (no remainder), it will break and print "num IS NOT a prime number.".
If the program detects a remainder, it will keep looping until it reaches the last number (n//2). If it does not detect 0 (no remainder), it will print "num IS a prime number.".
