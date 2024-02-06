#list operations
#  Create two lists of numbers
list1 = [1,  3,  5,  7,  9]
list2 = [2,  4,  6,  8,  10]
combined_list = list1 + list2
sorted_list = sorted(combined_list)
reversed_list = sorted_list[::-1]
unique_list = list(set(reversed_list))
# Print the final list
print(unique_list)

#Dictionaries 
#Dictionary creation 
person = {
    "name": "obi tobenna",
    "age":  21,
    "country": "Nigeria",
    "occupation": "Software Developer"
}

# Print the dictionary
print(person)


#Dictionary operations:
# Assuming the existing dictionary is named 'person'
person['email'] = 'obitobenna6@gmail.com'  # Adding a new key-value pair for the email address
person['age'] =  35  # Updating the person's age to a new value

# Print the updated dictionary
print(person)


# Existing dictionary
person = {
    "name": "John Doe",
    "age":   30,
    "country": "USA",
    "occupation": "Software Developer"
}

# Adding a new key-value pair for the email address and updating the person's age
person['email'] = 'obitobenna6@gmail.com'


#Dictionary iteration 
shopping_list = {
    "apples":  5,
    "bananas":  3,
    "milk":  1,
    "bread":  2,
    "cheese":  1
}
for item, quantity in shopping_list.items():
    print(f"{item}: {quantity}")


#Dictionary manipulation 
# Define two shopping lists as dictionaries
shopping_list1 = {
    "apples":  5,
    "bananas":  3,
    "milk":  1
}

shopping_list2 = {
    "bread":  2,
    "cheese":  1
}

# Merge the two dictionaries into one
merged_list = shopping_list1 | shopping_list2
# Remove a specific item from the merged dictionary
if 'milk' in merged_list:
    del merged_list['milk']
# Print the updated merged dictionary
print(merged_list)    

#Dictionary comprehension 
squares = {x: x**2 for x in range(1,  6)}
print(squares) 






