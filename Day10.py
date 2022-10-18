#Minimum pizza
for i in range(int(input())):
    a,b=map(int,input().split())
    result=a*b
    if result%4==0:
        print(result//4)
    else:
        print((result//4)+1)
