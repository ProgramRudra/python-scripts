cars = {
    'Lamborghini': ['Hurricane', 'Avetandor'],
    'Mercedes': ['GLK350', 'GLK450'],
    'Honda': ['Pilot', 'CR-V']
}

food = {
    'Vegan': ['Leaves', 'Fruits', 'Vegetables'],
    'Vegetarian': ['Been Burrito', 'Vegetables', 'Milk'],
    'Meat': ['Chicken', 'Beef', 'Pork']
}

counter1 = 0

for element in range(len(food['Vegan'])):
    a = food['Vegan'][counter1]
    #print(a)
    counter2 = 0
    for item in range(len(food['Vegetarian'])):
        b = food['Vegetarian'][counter2]
        if a==b:
            print('Match Found',a,b)
            counter2 += 1
        else:
            counter2+=1
    counter1+=1
