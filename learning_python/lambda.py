# func= lambda a: a+5
square =lambda x:x*x
# sum = lambda a,b,c:a+b+c

# x=3
# print(func(x))
# print(square(x))
# print(sum(x,1,2))

# list=["yashika", " vedant","yashraj","sanya","sakshi","vaibhav","shraddha" ]
# sentance=" ~~~~~ ".join(list)
# print(sentance)
# print(type(sentance))
# name=" good girl "
# classed="of class 111"
# a=f"yashika is a {name}"
# print(a)
# a="yashika is a {} {}".format( classed,name)
# print(a)

# l=[1,2,3,4]
# l1=[]
# for item in l:
#     l1.append(square(item))

# print(l1)
# print(list(map(square,l)))

# def greater(num):
#     if(num>5):
#         return True
#     else:
#         return False
# g10=lambda num:num>1
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(greater,l)))
# print(list(filter(g10,l)))

from functools import reduce
sum=lambda a,b:a+b
l=[1,2,3,4]
val=reduce(sum,l)
print(val)

