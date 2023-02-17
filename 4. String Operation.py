#Use Slicing to find the first 4 element of following str 

letters = "ABCDEFGHIJ"
print(letters[0:4]) #ABCD

#Use a stride value of 2 to find odd number
numbers = "123456789"
print(numbers[::2]) #find odd element on numbers

#use upper() to convert string into UPPERCASE
print("uppercase")
print("uppercase".upper())

#find index of the element. REMEMBER : start from 0
print("123456789".find("3"))

#indexing
name = "John doe"

#print the first element of name
print(name[0])

#print the fifth element of name
print(name[5])

#negative indexing
#lets use name again
#print the last element of name
print(name[-1])

#print the second element from last of name
print(name[-2])

#print every second element in the range from index 0 to index 5
print(name[0:5:2])

#Concatenate / Combine String
first_name = "John"
last_name = "Doe"
full_name = first_name+last_name #JohnDoe
print(full_name)

#Print string for 3 times
print(full_name*3)

#ESCAPE SEQUENCES

#use \n to new line escape sequences
print("John \nDoe")

#use \t to Tab Escape Sequences
print("John Doe \t is the best")

#use double backslach (\\) to include backslash
print("John Doe \\ is the best")
#Or place r
print(r"John Doe \ is the best")

#STRING OPERATION

#Convert all str to uppercase
a = "abcdefGhij"
print("before upper:", a)
b = a.upper()
print("after upper", b)

#Replace old substring with the new one
c = "John Doe"
print(c)
print("Replace John with Alex")
d = c.replace("John", "Alex")
print(d)

#Find the substring in strin
print(c.find("hn")) #2 because index of h
print(c.find("fnbewjfbfuewh")) #-1 because the substring is not in the string

