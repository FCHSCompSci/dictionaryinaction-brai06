car = {
    'type:': "type",
    'color:': "color",
    'amount:': "amount"
    }
while True:
    print("Welcome to Forever Car Dealer")
    car_buyer = input("Would you like to [s]hop,[p]ick up or [l]eave? ")
    if car_buyer == 's':
        car_type = input("What type of car would you prefer? ")
        car_color = input("What color would you prefer? ")
        car_amount = input("Hom many cars do you want to buy? ")
        car['type:'] = car_type
        car['color:'] = car_color
        car['amount:'] = car_amount
    elif car_buyer == 'p':
        for k,v in car.items():
            print(k,v)
    else:
        break
