#building race
for i in range(int(input())):
    a,b,x,y=map(int, input().split())
    chef=a/x 
    chefina=b/y 
    if chef<chefina:
        print("chef")
    elif chef>chefina:
        print("chefina")
    elif chef==chefina:
        print("both")
