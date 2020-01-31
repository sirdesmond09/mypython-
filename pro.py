print("WELCOME TO MATHCALS")
operations=['Add', 'Sub', 'Mult', 'Divi']
print(operations)
g=1
q=int(input("Choose the number of times you want to solve "))
while g<=q:
    gee=input("choose your arthimetric operation")
    if (gee==operations[0]):
        w=int(input("are you adding 2 or 3 numbers"))
        if (w==2):
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            def sum2(p,r):
                ans=(p+r)
                return ans
            print(sum2(a,b))
        elif(w==3):
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            c=int(input("enter third number"))
            def sum3(x,y,z):
                ans=(x+y+z)
                return ans
            print(sum3(a,b,c))
        else:
            print("wrong input")
    elif (gee==operations[1]):
        t=int(input("are you subtracting 2 or 3 numbers"))
        if (t==2):
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            def sub2(p,r):
                minus=(p-r)
                return minus
            print(sub2(a,b))
        elif(t==3):
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            c=int(input("enter third number"))
            def sub3(x,y,z):
                minus=(x-y-z)
                return minus
            print(sub3(a,b,c))
        else:
            print("wrong input")
    elif (gee==operations[2]):
        l=int(input("are you multiplying 2 or 3 numbers"))
        if (l==2):
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            def pro2(p,r):
                multiply=(p*r)
                return multiply
            print(pro2(a,b))
        elif(l==3):
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            c=int(input("enter third number"))
            def pro3(x,y,z):
                multiply=(x*y*z)
                return multiply
            print(pro3(a,b,c))
        else:
            print("wrong input")
    elif (gee==operations[2]):
        h=int(input("are you dividing 2 or 3 numbers"))
        if (h==2):
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            def quo2(p,r):
                divide=(p/r)
                return divide
            print(quo2(a,b))
        elif(h==3):
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            c=int(input("enter third number"))

            def quo3(x,y,z):
                divide=(x/y/z)
                return divide
            print(quo3(a,b,c))
        else:
            print("wrong input")
    else:
        print("Invalid input")
    g=g+1
print("Thanks for running my code")

