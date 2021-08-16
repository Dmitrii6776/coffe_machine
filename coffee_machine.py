from data import MENU, resources, unit_measure

is_off = False
def chose_coffee():
    comand = input('What would you like? (espresso, latte, cappuccino):  ').lower()
    return comand


def insert_coins(user_comand):
    try:
        if 0 < resources['Money'] >= MENU[user_comand]['cost']:
            return resources['Money']
    except Exception:
        print('Please insert coins.')
        quarters = int(input('How many quarters?:  '))
        dimes = int(input('How many dimes?:  '))
        nickles = int(input('How many nickles?:  '))
        pennies = int(input('How many pennies?:  '))
        balance = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
        resources['Money'] = round(balance, 2)
        return round(balance, 2)


def check_resources(user_comand):
    make_coffee0 = False
    water = MENU[user_comand]['ingredients']['water']
    coffee1 = MENU[user_comand]['ingredients']['coffee']
    if user_comand == 'espresso' and resources['water'] >= water and resources['coffee'] >= coffee1:
        make_coffee0 = True
        return make_coffee0
    elif resources['water'] >= water and resources['milk'] >= MENU[user_comand]['ingredients']['milk'] \
            and resources['coffee'] >= coffee1:
        make_coffee0 = True
        return make_coffee0
    elif resources['water'] < water:
        return 'water'
    elif resources[coffee1] < coffee1:
        return 'coffee'
    elif resources['milk'] < MENU[user_comand]['ingredients']['milk']:
        return 'milk'


def check_balance(user_comand):
    user_balance = resources['Money']
    make_coffee2 = False
    if MENU[user_comand]['cost'] > user_balance:
        return "Sorry that's not enough money. Money refunded."
    elif user_balance <= 0:
        return "Sorry that's not enough money. Money refunded."
    elif user_balance >= MENU[user_comand]['cost']:
        make_coffee2 = True
        return make_coffee2


def make_coffee():
    while not is_off:
        user_comand = chose_coffee()
        if user_comand == 'off':
            is_off == True
            return is_off
        if user_comand == 'report':
            for i in resources:
                print(f'{i}: {resources[i]} {unit_measure[i]}')
            return make_coffee()

        cost = MENU[user_comand]['cost']
        user_balance = insert_coins(user_comand)
        user_resources = check_resources(user_comand)
        quantity_resources = check_balance(user_comand)

        if user_resources == True and quantity_resources == True:
            print(f"Here is ${user_balance} in change.")
            print(f"Here is your {user_comand}️. Enjoy!")
            resources['Money'] -= round(cost, 2)
            resources["water"] -= MENU[user_comand]["ingredients"]['water']
            resources['coffee'] -= MENU[user_comand]["ingredients"]['coffee']
            if user_comand != 'espresso':
                resources['milk'] -= MENU[user_comand]["ingredients"]['milk']
        elif user_resources != True:
            print(f"Sorry there is not enough {user_resources}.")
        elif not quantity_resources:
            print(f"user_q {quantity_resources}")
        else:
            print(f"user_res {user_resources}")





make_coffee()