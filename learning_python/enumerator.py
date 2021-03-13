# list1=[1,3,4,"yashika", False,"6.7"]

# for index, item in enumerate(list1):
#     print(item , index)

# a=[3,4,5,67,22,66,222,88,33,9]
# # b=[]
# # for item in a:
# #     if item%2==0:
# #         b.append(item)
# n=[i for i in a if i%2==0]
# print(n)

# list=[1,2,3,4,5,6,7,8,9,10]
# for index , item in enumerate(list):
#     if index==2 or index==4 or index==6:
#         print(index,item)

num=int(input("Enter a number:\n"))
table=[num*i for i in range(1,11)]
print(table)

