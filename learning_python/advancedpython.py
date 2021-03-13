# while(True):
#     print("press q to quit")
#     s=input(" enter a number : \n")
#     if(s=='q'):
#         break
#     try:
#        s=int(s)
#        if(s>6):
#            print("you have entered a number greater than 6")
#     except Exception as e:
#         print(f"your input resulted in an error {e}")

# print("thanks for playing this game")

try:
    a=int(input("enter a number:"))
    c=1/a
    print(c)
except ValueError as e:
    print("Exception1 occured")
    print(e)
except ZeroDivisionError as e:
    print("Exception2 occured")
    print(e)

print("thankss!!")