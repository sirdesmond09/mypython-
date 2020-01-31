#the first letter varies from A to C
for first in "ABC":
    for second in "ABC": #the second varies from A to C
        if second != first: #no duplicate of letters
            for third in "ABC": #the third varies from A to C
            #dont duplicate second letter
                if third != first and third != second:
                    print (first + second + third)
l=['a', 'b', 'c', 'd', 'e', 'f']
print(l[0:4])
print(l[:])
