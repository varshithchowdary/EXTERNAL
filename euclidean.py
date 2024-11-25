def euclidean(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def advanced_euclidean(a,b):
    if a==0:
        return b,0,1
    gcd,x1,y1=advanced_euclidean(b%a,a)
    x = y1 - (b//a) * x1
    y=x1
    return gcd,x,y
print("a:")
a=int(input())
print("b:")
b=int(input())
print(euclidean(a,b))
print(advanced_euclidean(a,b))

    