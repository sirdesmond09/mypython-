def main_goods():
        profit=1000
        exchange_rate=1333
 
        china_price=float(input("how much? "))
        shipping_fee=float(input("shipping fee? "))
        number_of_goods=float(input("How many? "))
        one_without_profit= ((((((china_price+shipping_fee)*number_of_goods)+3+5.6)*58)+exchange_rate)/number_of_goods)
        print(f"The value for one without our profit is #{one_without_profit}")
        all_without_profit=(((((china_price+shipping_fee)*number_of_goods)+3+5.6)*58)+exchange_rate)
        print (f"The value for all without profit is #{all_without_profit}")
        our_price=(one_without_profit+profit)
        print (f"The minimum amount to sell is #{our_price}")  


def lesser_goods():
        profit=1300
        exchange_rate=604.44

        china_price=float(input("how much? "))
        shipping_fee=float(input("shipping fee? "))
        number_of_goods=float(input("How many? "))
        one_without_profit= ((((((china_price+shipping_fee)*number_of_goods)+3+2.4)*58)+exchange_rate)/number_of_goods)
        print (f"The value for one without our profit is #{one_without_profit}")
        all_without_profit=(((((china_price+shipping_fee)*number_of_goods)+3+2.4)*58)+exchange_rate)
        print (f"The value for all without profit is #{all_without_profit}")
        our_price=(one_without_profit+profit)
        print (f"The minimum amount to sell is #{our_price}")      

option = [ "begin", "cancel" ]

a = option[0]
b = option[1]

while True:
    print("Click 'Begin' to begin and 'Cancel' to cancel")
    choice = input("> ").lower()
    if choice == a:
        try: 
                option1 = ['main', 'others', 'back']
                print("Click 'main' to calculate for main goods and 'others' to calculate for other goods")
                print("click 'Back' to go back")
                while True:
                        choice1 = input("> ").lower()    
                        x = option1[0]
                        y = option1[1]
                        z = option1[2]
                
                        if choice1 == x:
                                main_goods()
                        elif choice1 == y:
                                lesser_goods()
                        elif choice1 == z:
                                break       
                        else:
                                print("Try again!")    
        except:
                ValueError 
                pass   
    elif choice== b:
            break
    else:
            print("Try again")

