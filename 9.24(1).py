x=int(input())
while x!=1:
    if x%2==0:
        x=int(x/2)#谨防出现不必要的.0
        print(f"{2*x}/2={x}")
    else:
        print(f"{x}*3+1={int(3*x+1)}")
        x=3*x+1