# name=input("enter your name")
# marks=int(input("enter your marks"))
# phonenumb=int(input("enter your number"))

# a= "The name of the student is {} , his marks are {} and his phone number is {}".format(name,marks,phonenumb)
# print(a)
# l=[str(i*7) for i in range(1,11)]
# print(l)

# vertical="\n".join(l)
# print(vertical)
# lis=[1,2,3,456,7788,655454,789,2343,345,10,78,90,50,25]
# div=lambda n:n%5==0

# print(list(filter(div,lis)))
from functools import reduce

lis=[1,2,34,5,6,11,78,44,33,11,899,9]
a=reduce(max,lis)
print(a)
