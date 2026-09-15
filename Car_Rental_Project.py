import copy
#Actual list and we are not mutating it. 
car_rental_db = [
    {
        "model": "Pajero",
        "available": 2,
        "per_day_price": 150,
        "liability_inc_per_day": 30,
        "comprehensive_inc_per_day": 70

    },
    {
        "model": "Altima",
        "available": 2,
        "per_day_price": 70,
        "liability_inc_per_day": 20,
        "comprehensive_inc_per_day": 50

    },
    {
        "model": "Camry ",
        "available": 3,
        "per_day_price": 90,
        "liability_inc_per_day": 20,
        "comprehensive_inc_per_day": 50

    },
]

available_cars_data = copy.deepcopy(car_rental_db)

total_opreations = [] 

#Displaying Menu
def start_app():
    print(f'MAIN MENU\n1-Car Rent\n2-Car Return\n3-Print the totals')
    bussiness_logic()

#Displaying Options
def bussiness_logic():
    option = input("Enter your option: ")
    if (option == '1'):
        car_rent()
    elif (option == '2'):
        car_return()
    elif (option == '3'):
        print_totals()
    else:
        print("Invalid MENU option")
        return start_app()

#Displaying Cars Data
def menu(cars_data):
    print('--------------------------------------------------------------------------------------------------------------------')
    print(f'Model\t\t\tAvailable\tPrice/day\tLiability insurance/day\t\tComprehensive insurance/day')
    print('--------------------------------------------------------------------------------------------------------------------')
    i = 0
    for data in cars_data:
        i += 1
        print(f"{i}.{data['model']}\t\t{data['available']}\t\t{data['per_day_price']}\t\t\t{data['liability_inc_per_day']}\t\t\t\t\t{data['comprehensive_inc_per_day']}")

#Asking for display more options
def more_options():
    final_car = input("More Options(Y/N)").upper()
    if (final_car == 'Y'):
        start_app()
    elif (final_car == 'N'):
        return
    else:
        return more_options()

#Selecting a car for rent
def car_rent():
    menu(available_cars_data)
    
    try:
        car_type = int(input('Enter Car Type: '))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return car_rent()
        
    if (car_type <= 0 or car_type > len(available_cars_data) or available_cars_data[car_type - 1]["available"] <= 0):
        print(f'No Car of type {car_type} is available')
        return car_rent()
    
    
    try:
        no_days = int(input('Enter the no of days: '))
    except ValueError:
        print("Invalid input! Please enter a valid number for days.")
        return car_rent()
        
    ins_type = input(
        "Enter L for liability and F for full insurance: ").upper()
    rent_cost = available_cars_data[car_type - 1]["per_day_price"] * no_days
    ins_cost = 0
    
    
    if (ins_type == 'L'):
        ins_cost = available_cars_data[car_type - 1]["liability_inc_per_day"]
    elif (ins_type == 'F'):
        ins_cost = available_cars_data[car_type - 1]["comprehensive_inc_per_day"]
    else:
        print("Invalid Insurance type")
        return car_rent()
        
    tax = rent_cost * 0.05
    total_bill = rent_cost + ins_cost + tax

    print('-----------------------------------------------------------------------------------')
    print(
        f"Rent Cost: {rent_cost} PKR\nInsurance Cost: {ins_cost} PKR\nTax: {tax} PKR")
    print('-----------------------------------------------------------------------------------')
    print(f'Total: {total_bill} PKR')
    print('-----------------------------------------------------------------------------------')

    total_opreations.append({
        "model": available_cars_data[car_type - 1]['model'],
        "rent_cost": rent_cost,
        "ins_cost": ins_cost,
        "tax": tax,
        "total_cost": total_bill,
        "rent_days": no_days
    })

    available_cars_data[car_type - 1]["available"] -= 1

    more_options()

#Returning car which we took on rent
def car_return():
    i = 0
    print('Select what type of car is returned')
    for data in available_cars_data:
        i += 1
        print(f"{i}: {data['model']}")
        
    try:
        car_type = int(input('Enter car type: '))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return car_return()
        
    if car_type > len(available_cars_data):
        print(f'No Car of type {car_type} is available')
        return car_return()
        
    if available_cars_data[car_type - 1]["available"] < car_rental_db[car_type - 1]["available"]:
        available_cars_data[car_type - 1]["available"] += 1
    else:
        print("Invalid car return")
        return more_options()
        
    menu(available_cars_data)
    more_options()

#Printing the total Bill
def print_totals():
    if len(total_opreations) > 0:
        print('--------------------------------------------------------------------------------------')
        print(f'Model\tAvailable\tPrice/day\tLiability insurance/day\t\tComprehensive insurance/day')
        print('--------------------------------------------------------------------------------------')
        i = 0
        for data in total_opreations:
            i += 1
            print(
                f"{i}.{data['model']}\t{data['rent_cost']}\t{data['ins_cost']}\t\t{data['tax']}\t\t\t\t{data['total_cost']}\t{data['rent_days']}")
        total_income = 0
        total_insurance = 0
        total_tax = 0
        for car_total in total_opreations:
            total_income += car_total["rent_cost"]
            total_insurance += car_total["ins_cost"]
            total_tax += car_total["tax"]
        print('--------------------------------------------------------------------------------------')
        print(
            f"Total Income: {total_income} PKR\nTotal Insurance: {total_insurance} PKR\nTotal Tax: {total_tax} PKR")
        print('--------------------------------------------------------------------------------------')
        more_options()
    else:
        print('No data found')
        start_app()


start_app()
