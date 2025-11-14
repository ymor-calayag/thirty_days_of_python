# Exercises: Level 1
# Declare an empty list
lst = list()

# Declare a list with more than 5 items
numbers = [1, 2, 3, 4, 5]

# Find the length of your list
print(len(numbers))

# Get the first item, the middle item and the last item of the list
def get_items(items):
    items_copy = items.copy()
    print(f"First Item: {items_copy[0]}")
    middle_index = len(items_copy) // 2
    print(f"Middle Item: {items_copy[middle_index]}")
    print(f"Last Item: {items_copy[-1]}")

get_items(numbers)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Jeff', 29, 1.6, 'Married', 'La Union']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
get_items(it_companies)

# Print the list after modifying one of the companies
it_companies_copy = it_companies.copy()
it_companies_copy.pop()
print(it_companies_copy)

# Add an IT company to it_companies
it_companies.append("App Brewery")
print(it_companies)

# Insert an IT company in the middle of the companies list
mid_index = len(it_companies) // 2
it_companies.insert(mid_index, "Tech Town")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined_copy = it_companies.copy()
lst_to_str = "#;  ".join(joined_copy)
print(lst_to_str)

# Check if a certain company exists in the it_companies list.
print('facebook' in [company.lower() for company in it_companies])

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
copy_for_slicing = it_companies.copy()
print(copy_for_slicing[3:])

# Slice out the last 3 companies from the list
print(copy_for_slicing[:-3])

# Slice out the middle IT company or companies from the list
new_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mid_item_index = len(new_numbers_list) // 2
if len(new_numbers_list) % 2 == 0:
    print(new_numbers_list[mid_item_index - 1:mid_item_index + 1])
else:
    print(new_numbers_list[mid_item_index:mid_item_index + 1])

# Remove the first IT company from the list
it_companies_copy.pop(0)
print(it_companies_copy)

# Remove the middle IT company or companies from the list
new_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mid_item_index = len(new_numbers_list) // 2
if len(new_numbers_list) % 2 == 0:
    print(new_numbers_list[mid_item_index - 1:mid_item_index + 1])
else:
    print(new_numbers_list[mid_item_index:mid_item_index + 1])

# Remove the last IT company from the list
it_companies_copy.pop()
print(it_companies_copy)

# Remove all IT companies from the list
it_companies_copy.clear()
print(it_companies_copy)

# Destroy the IT companies list
del it_companies_copy

# # Join the following lists:
# # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# # back_end = ['Node','Express', 'MongoDB']
# # After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

def joining_list(lst_one, lst_two):
    front_end_copy = lst_one.copy()
    back_end_copy = lst_two.copy()
    full_stack = front_end_copy + back_end_copy

    redux_index = full_stack.index('Redux')
    full_stack.insert(redux_index + 1, 'Python')
    full_stack.insert(redux_index + 2, 'SQL')
    print(full_stack)

joining_list(front_end, back_end)

# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_copy = ages.copy()

print(ages_copy)
ages_copy.sort()
print(ages_copy)
print(min(ages_copy))
print(max(ages_copy))

min_age = min(ages_copy)
max_age = max(ages_copy)

# Add the min age and the max age again to the list
ages_copy.append(min_age)
ages_copy.append(max_age)
print(ages_copy)

# Find the median age (one middle item or two middle items divided by two)
def find_median(lst):
    lst_copy = lst.copy()
    mid_of_list = len(lst_copy) // 2

    if len(lst_copy) % 2 == 0:
        print(lst_copy[mid_of_list - 1: mid_of_list + 1])
    else:
        print(lst_copy[mid_of_list])

find_median(ages)


# Find the average age (sum of all items divided by their number)
#Short way
print(sum(ages) / len(ages)) 
#long way
total = 0
for i in ages:
    total += i
print(f"Average age: {total / len(ages)}")

# Find the range of the ages (max minus min)
print(f"Range of ages: {max_age - min_age}")

# Compare the value of (min - average) and (max - average), use abs() method
average = sum(ages) / len(ages)
print(abs(max_age - average))
print(abs(min_age - average))

# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
find_median(countries)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
def divide_list(lst):
    lst_copy = lst.copy()
    lst_midle_item = len(lst_copy) // 2

    if len(lst_copy) % 2 == 0:
        first_half = lst_copy[0:lst_midle_item]
        second_half = lst_copy[lst_midle_item:]
        print(first_half)
        print(second_half)
    else:
        first_half = lst_copy[0:lst_midle_item + 1]
        second_half = lst_copy[lst_midle_item + 1:]
        print(first_half)
        print(second_half)

divide_list(countries)


# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first, second, third, *scandic = countries
print(first, second, third, scandic)