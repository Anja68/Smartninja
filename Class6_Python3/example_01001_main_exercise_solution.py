# adjust the following code
# so that it is suitable
# for importing

def add_10(x):
    x +=10
    return x


if __name__=="__main__":
    x=10
    y=20
    z=30
    a=add_10(x)
    b=add_10(y)
    c=add_10(z)
    print("a =",a)
    print("b =",b)
    print("c =",c)