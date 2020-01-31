print("WELCOME TO MY FOOD GUIDE")
print("I am Chef Dessy")
I=input(str("Do you want to try out this guide?, type 'YES' to explore or 'NO' to exit"))
if(I=="YES"):
    print("Enjoy the unlimited possibilites as we take you on this journey to deliciousness")
elif(I=="NO"):
    print("It was awesome interacting with you, we hope you follow us on the journey to deliciousness soomeday")
    exit()
else:
    print("invalid selection")
food=["rice","beans","yam"]
print(food)
foodlist= input("enter your food type")
if(foodlist==food[0]):
    a=input("Do you want to prepare jollof or fried rice?")
    if(a=="jollof"):
        print("this is how to prepare jollof rice")
        print("Step 1")
        print("fry your tomatoes, onions etc")
        print("Step 2")
        print("put in your hot water")
        print("Step 3")
        print("put in your rice and leave to boil")
    elif(a=="fried rice"):
        print("this is how to prepare fried rice")
        print("Step 1")
        print("perboil the rice with salt and thyme, then seive it")
        print("Step 2")
        print("leave it to boil")
    else:
        print("invalid input")
elif(foodlist==food[1]):
    print("this is how to prepare beans")
elif (foodlist==food[2]):
    print("this is how to prepare yam")
else:
    print("i dont know how to prepare it")
