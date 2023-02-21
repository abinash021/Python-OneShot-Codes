# Type-Casting in Python
# As we previously saw that two differrent types of datatypes cannot concatenate
# i.e. str to int (!not) 
# i.e. str to bool (!not) 
# etc...

# That's why we use type-casting during concatenation
# Type-casting Syntax:-
# typecasting_data_type(Variable)

# For example, your age is 17 years old in last two years
# And currently your age is 19 years old
# so, if we write a program like this:- 

###  PREVIOUS PROGRAM
##old_age = input("Enter your old age : ")
##new_age = old_age + 2
##print(new_age)

# Here an error shows that:- TypeError: can only concatenate str (not "int") to str
# i.e. it takes input the old_age in string format but we want it in integer format 
# To Avoid that error we use type casting:-->
old_age = input("Enter your old age : ")
new_age = int(old_age) + 2        #making old_age from str to int using Type-Casting
print(new_age)