size=int(input("enter table size"))
for row in range (1, size+1):
    for column in range (1, size+1):
        product=row*column
        print('{0:4}'.format(product),end='')
    print()
