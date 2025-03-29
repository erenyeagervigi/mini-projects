import data
import  arts

data_list = data.MENU
resource_list = data.resources
profits = 0

def data(value):
    print(f"Water: {value["espresso"]["ingredients"]["water"]} ml")
    print(f"Water: {value["espresso"]["ingredients"]["coffee"]} g")


def resourcess(value):
    print(f"water: {value["water"]} ml")
    print(f"milk: {value["milk"]} ml")
    print(f"coffee: {value["coffee"]} g")
    print(f"money: ${profits}")

def user_choice(user_needs):
    print(f"the cost of {user_needs} is : ${data_list[user_needs]['cost']} ")

def subtracting_resources(value, user_needs):
    supplies_water = value['water'] - data_list[user_needs]['ingredients']['water']
    value['water'] = supplies_water
    supplies_coffee = value['coffee'] - data_list[user_needs]['ingredients']['coffee']
    value['coffee'] = supplies_coffee
    # print(f"remaining water: {supplies_water}")
    # print(f"remaining coffee: {supplies_coffee}")
    try:
        supplies_milk = value['milk'] - data_list[user_needs]['ingredients']['milk']
        value['milk'] = supplies_milk
        # print(f"remaining milk {supplies_milk}")
    except KeyError:
        pass

def checking(user_needs):
    if resource_list["water"] > data_list[user_needs]['ingredients']['water']:
        if resource_list["coffee"] > data_list[user_needs]['ingredients']['coffee']:
            try:
                resource_list['milk'] > data_list[user_needs]['ingredients']['coffee']
            except KeyError:
                pass

            subtracting_resources(resource_list, user_needs)
            print("here's you coffee ☕")

    else:
        print("insufficient supplies")
        print("collect you're refunded money")
        print("come by next time!!")
        return False


def money(user_needs):

    user_choice(user_needs)

    money_1 = int(input("Enter the number of dollars you wanna enter: "))
    money_2 = int(input("Enter the number of cents you wanna enter: "))

    user_total_money = money_1 + (money_2/10)
    print(f"you're total : ${user_total_money}")

    global profits
    if user_total_money == data_list[user_needs]['cost']:
        profits += data_list[user_needs]['cost']
        checking(user_needs)

    elif user_total_money > data_list[user_needs]['cost']:
        change =  user_total_money - data_list[user_needs]['cost']
        print(f"here's your change {change}")
        profits += data_list[user_needs]['cost']
        checking(user_needs)

    else:
        print("insufficient money")
        print("collect you're refunded money")
        return False

def make_coffee():
    while True:
        user_needs = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_needs == "report" or user_needs == "r":
            resourcess(resource_list)
        elif user_needs == "espresso" or user_needs == "e":
            user_needs = "espresso"
            money(user_needs)

        elif user_needs == "latte" or user_needs == "l":
            user_needs = "latte"
            money(user_needs)

        elif user_needs == "c" or user_needs == "cappuccino":
            user_needs = "cappuccino"
            money(user_needs)

        elif user_needs == "off":
            print(arts.art1)
            break

def main():
    print(arts.art)  # Display ASCII art on startup
    make_coffee()


if __name__ == "__main__":
    main()
