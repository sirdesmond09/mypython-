import pymysql

connect = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "rockpaperscissors"
)

cursor = connect.cursor()
# sql_table = """CREATE TABLE players
#         (
#             id int PRIMARY KEY AUTO_INCREMENT,
#             names varchar (50),
#             status varchar (50)
#         )

# """
# cursor.execute(sql_table)


def begin():
    G=['rock', 'paper', 'scissors']
    y=1    
    a=0
    b=0
    d=0
    print("Rock, Paper, Scissors!")
    while y<=5:
        print("What's your choice?")
        P1=input("> ").lower()
        print(P1)
        import random
        r=random.choice(G)
        print(f"Computer chose {r}")
        if(P1==G[0] and r==G[0]):
            print("draw")
        elif(P1==G[1] and r==G[1]):
            print("draw")
        elif(P1==G[2] and r==G[2]):
            print("draw")
        elif(P1==G[0] and r==G[2]):
            print("player wins")
            a=a+1
        elif(P1==G[1] and r==G[0]):
            print("player wins")
            a=a+1
        elif(P1==G[2] and r==G[1]):
            print("player wins")
            a=a+1
        elif(P1==G[0] and r==G[1]):
            print("computer wins")
            b=b+1
        elif(P1==G[1] and r==G[2]):
            print("computer wins")
            b=b+1
        elif(P1==G[2] and r==G[0]):
            print("computer wins")
            b=b+1
        else:
            print("invalid entry")
        y+=1

    result = [ 'winner', 'loser', 'no winner' ]
    if(a>=2 and  b<2):
        score = result[0]
        print(score)
        try_again()
    elif(b>=2 and a<2):
        score = result[1]
        print(score)
        try_again()
    else:
        score = result[2]
        print(score)
        try_again()
    print("Game over")


def help():
    print("""
Rock Paper Sciccors a.k.a RPS is a very simple game to play
You can start by clinking 'B'
You only have 5 chances after which the result would be announced!
Good Luck!    
    """)

def try_again():
    while True:     
        again = ['y', 'n']
        print("Try again? Y or N")
        option_try = input('> ').lower()
        if option_try == again[0]:
            begin()
        elif option_try == again[1]:
            break
        else:
            print("Invalid input")

        


print("WELCOME TO RPS!")
name = input("Enter your name: ")
options = ['h', 'b', 'end']
while True:
    print("click 'h' for help, 'B' to begin or 'end' to quit")
    option = input("> ").lower()
    if option==options[0]:
        help()
    elif option == options[1]:
        begin()
    elif option == options[2]:
        break
    else:
        print("Try again")


sql_insert = f""" INSERT INTO players
            VALUES ({name}, %s )
 """
status = [ 'winner', 'no winner', 'loser' ]
if status == f"{score}":
    db_status = status

cursor.executemany( sql_insert, db_status )  

connect.commit()
connect.close

