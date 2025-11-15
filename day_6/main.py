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
family_members.insert(0, "Father")
family_members.append("Mother")
tuple(family_members)
print(family_members)