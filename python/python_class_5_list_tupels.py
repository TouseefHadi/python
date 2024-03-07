########################################listssssss############################################################

## list with numbers
list = [1,2,3,4,5,6,7]
print("elements of the list", list[0])
print("\nElement of the list in range", list[0:2]) ## indexing is starting from zero and when we write the last number in range like 2 here will exluded
print("\ndata type of the elements inside the list is: ", type(list[0]))


#list with string
student = ["ali", "asad", "javad", "uzair"]
print("\nName of the first students is: ", student[0])
print("\n length of the entire list is: ", len(student))
print("\ndata type of the elements inside the list is: ", type(student[0]))

#List with different data types
employee = ["Ahmad", 2000, "ahmad123@gmail.com", 3012232323]
print("length of the list is given that: ", len(employee))
print("The name of the employee is: ", employee[0])
print("Email adress of the emplyee is: ", employee[2])


###########Tuplesss############################################################################################


## tuples with numbers
tuples = (1,2,3,4,5,6)
print("\nelements of the list", tuples[0])
print("\nElement of the list in range", tuples[0:2]) ## indexing is starting from zero and when we write the last number in range like 2 here will exluded
print("\ndata type of the elements inside the list is: ", type(tuples[0]))

#tuples with string

studentsss = ("ali", "asad", "javad", "uzair")
print("\nName of the first students is: ", studentsss[0])
print("\n length of the entire list is: ", len(studentsss))
print("\ndata type of the elements inside the list is: ", type(studentsss[0]))


#tuples with different data types
employeesss = ("Ahmad", 2000, "ahmad123@gmail.com", 3012232323)
print("\nlength of the list is given that: ", len(employeesss))
print("The name of the employee is: ", employeesss[0])
print("Email adress of the emplyee is: ", employeesss[2])



##########################difference between them #########################################################################
# Lists are mutible means they are modified and customizable but tuples are not.

############lets modified the lists####################
list_school_teachers = ["sir Ahmad", "sir Asad", "sir ali", "sir azam"]
print("Original list:", list_school_teachers)

# Create a copy of the original list
new_list_1 = list_school_teachers.copy() ## we need copy here because the append function directly modified the list and unable to assig the resultant value into the new varaible

# Append "bilal" to the new list
new_list_1.append("sir bilal")

# Print the new list
print("New list with 'bilal' added:", new_list_1)


#### lets say sir asad leave the school than we have to delete him from our list so we willl do it like this, we need another copy of the list
new_list_2 = new_list_1.copy()
del new_list_2 [1]
print("now the sir asad is deleted from the list!" , new_list_2)

############ lets say we have another teacher come to our school sir rana and sir rana has same subject as sir azam and we want to kept sir rana instead of sir azam so we will use modification
new_list_3 = new_list_2.copy()
new_list_3[2] = "sir rana"
print("lets see the modification: ", new_list_3)

