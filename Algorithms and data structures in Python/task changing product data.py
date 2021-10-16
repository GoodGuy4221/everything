warehouse_dict = {
    1: ['book', 1, 500],
    2: ['pen', 3, 10000],
    3: ['iphone', 5, 20],
    4: ['hat', 4, 50],
    5: ['shoes', 6, 5],
}

ended = False
while not ended:
    number_of_changing_product = int(input('Enter the number of the item you want to change '))
    if warehouse_dict.get(number_of_changing_product):
        warehouse_dict[number_of_changing_product][2] = int(input('Enter a new quantity of the product '))
        print(warehouse_dict[number_of_changing_product])
    elif number_of_changing_product == 0:
        ended = True
    else:
        print('Incorrect product number entered')
