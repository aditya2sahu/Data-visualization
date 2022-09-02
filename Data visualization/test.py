# num=int(input("Enter"))
#
# for x in range(num):
#     print("A"*(num-x-1),)
#     for i in range(2*x+1):
#         if i%2!=0:
#             print("*",end="")
#         else:
#             pass


num=5
for x in range(1,num):
    print(" "*(num-x-1),"*"*x)