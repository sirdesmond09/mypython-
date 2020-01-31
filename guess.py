# GUESS GAME
guess_count=0
secret_num=5
guess_limit=3
while guess_count < guess_limit:
    guess = int(input ("Guess: "))
    guess_count += 1
    if guess == secret_num:
        print("you win")
        break
else:
    print("you lose")

# CAR GAME
option1= "help"
option2= "start"
option3 = "stop"
option4 = "quit"
Car_started = False
while True:
    command = input("> ").lower()
    if command == option1:
        print(""" 
    start - To start the car
    stop - To stop the car
    quit - To exit
    """)
    elif command == option2:
        if Car_started:
            print ("car is already started")
        else:
             Car_started = True
             print("you car has started!")
    elif command == option3:
        if not Car_started:
            print("your car is already stopped")
        else:
            Car_started = False
            print("Car stopped!")
    elif command == option4:
        break
    else:
        print("i don't understand")

# using for loops to get F and L
number =[5, 2, 5, 2, 2]
for x_count in number:
    output = ''
    for count in range (x_count):
        output += 'x'
    print(output)
number =[2, 2, 2, 2, 5]
for x_count in number:
    output = ''
    for count in range (x_count):
        output += 'x'
    print(output)

# maximum number
number1 =[2, 3, 10, 2, 5]
max = number1[0]
for num in number1:
    if num > max:
        max = num
print (max)

