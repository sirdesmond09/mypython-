def famous():
    print("this is a function") # defining a function
#calling the function
famous()

def reed():
    print("you are underaged")
guy=int(input("enter your age"))
if guy <= 10:
    reed()
else:
    print("welcome on board")
#assigning numbers to variables in a function
def boy(x,y):
    l=[x+y, x*y]
    return l
print (boy(4,2))

#simple interest
g=1
while g <=3:
    def interest(p,r,t):
        ans=(p*r*t)/100
        return ans
    print(interest(64980,10,2))
    a=input(int("enter your principal:"))
    b=input(int("enter your interest rate:"))
    c=input(int("enter your time frame:"))
    print(interest(a,b,c))
    g=g+1
#functions reduce code complexity in our programs
