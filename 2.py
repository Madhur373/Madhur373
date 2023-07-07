# number=int(input("Enter a number"))
# i=0
# while i<=10:
#     print(number,"x",i,"=",number*i)
#     i=i+1

# l=["harry","salman","siya","Sakshi","hardik","Virat"]
# l1=[]
# for i in l:
#     if i[0]=="s" or i[0]=="S":
#         print("hello",i)
#         l1.append(i)
# print(l1)

# l=["harry","salman","siya","sakshi","hardik","Virat"]
# l1=[]
# i=0
# while i<len(l):
#     if l[i][0]=="s":
#         print("hello",l[i])
#         l1.append(l[i])
#     i=i+1

# print(l1)


#prime number

num=int(input("Enter Number"))
i=1
factor=1
while i<num:
    if num % i==0:
        factor=factor+1
    i=i+1
if factor>3:
    print("not a prime")
else:
    print("Prime")

