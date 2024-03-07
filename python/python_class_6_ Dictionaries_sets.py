################################################dictionriesss##############################################################

student_info = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "city": "New York"
}

print(student_info)
print("lets print name of the student: ", student_info["name"])
print("lets print grade of the student: ", student_info['grade'])


product_catalog = {
    "item1": {"name": "Chair", "price": 50},
    "item2": {"name": "Desk", "price": 100},
    "item3": {"name": "Lamp", "price": 20}
}


print("lets print the vlaues by thier keys" , product_catalog['item1'])
print("lets print a key value that is inside in another key" , product_catalog["item2"]["name"])

###############################################sets##################################################################

unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
####print(unique_numbers[0]) this line will not work here because sets not using the indexing method becasue set is defined as that it will have only unique values
test_set = {1,1,2,3,4,5,5}
print("for testing" , test_set) ## as u will se after this line execution that it remove the dublicates values

## if you want to check the specific value is preset in set or not u have to to use "in" like
print("it will give tru if nuber is present if not it will give us false ---->>>>>" , 5 in test_set)
