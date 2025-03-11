n = int(input())
#If n is odd, print Weird
if n % 2 != 0:
    print("Weird")

#If n is even and in the inclusive range of 2 to 5, print Not Weird
elif n % 2 == 0 and n in range(2, 6):
    print("Not Weird")

#If n is even and in the inclusive range of 6 to 20, print Weird
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")

#If n is even and greater than 20, print Not Weird
elif n % 2 == 0 and n > 20:
    print("Not Weird")
