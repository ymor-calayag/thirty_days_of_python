# Exercises: Level 1
# Create an empty tuple
tpl = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("bro_one", "bro_two")
sisters = ("sis_one", "sis_two")
print(brothers, sisters)

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
print(f"number of siblings: {len(siblings)}")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append("Father")
family_members.append("Mother")
tuple(family_members)
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
bro_one, bro_two, sis_one, sis_two, father, mother = family_members
print(bro_one, bro_two, sis_one, sis_two, father, mother)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("f1", "f2")
vegetables = ("v1", "v2")
animal_products = ("ap1", "ap2")
food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
def mid_item(lst):
    lst_copy = lst.copy()
    mid_index = len(lst_copy) // 2

    if len(lst_copy) % 2 == 0:
        print(lst_copy[mid_index - 1: mid_index + 1])
    else:
        print(lst_copy[mid_index:mid_index + 1])

mid_item(food_stuff_lt)

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt)
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# Delete the food_staff_tp tuple completely
print(food_stuff_tp)
del food_stuff_tp

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Iceland' in nordic_countries)
