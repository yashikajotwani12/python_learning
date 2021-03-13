# num=int(input("enter the number"))
# factorial=1
# for i in range(1, num):
#          factorial=factorial*i
# print(f"the factorial of the number is {factorial}")

# n=4
# for i in range(4):
#     print(" * " *(i+1))
n=3
for i in range(n):
   print(" "*(n-i-1), end=" ")
   print("*"*(2*i+1), end=" ")
   print(" "*(n-i-1))

