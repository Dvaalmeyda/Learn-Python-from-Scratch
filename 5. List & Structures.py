#TUPLES = Ordered Sequence, writtem as comma-separated elements withim parentheses ()
print("TUPLE \n")
number = ("df",2,3.8,4,True,6,7,8,9)
print(number) # ("df",2,3.8,4,True,6,7,8,9)

#Tuple type = tuple
print(type(number))

#TUPLES SLICING
#Accessing element on tuple via index
print(number[0]) # access the firs element of number'df'
print(number[-1]) #acess the last element of number 9
print(number[0:3]) #acces the first three elements of number ('df',2 ,3.8)

#Use len command to obtain the lenght of a tuple
print(len(number))

#Concatenae / Combine Tuple by adding them
number2 = number + ("apalah", 11)
print(number2)

#TUPLE : IMMUTABLE
print(number)
#number[2]="65" >>> tuples are immutable so we can't change it
#to manipulate it we have to create a new one, ex = number2
print(number2)

#Nested Tuple
nesting = (1,2,("keren","jaya"),[3,4.7],("gg",(True,2)))
#INDEX >>> 0|1||       2      | |  3  | |     4      |
#Sub-Index     |   0   |   1  | |0| 1 | |  0  |  1   |
#Sub-sub-Index                          |     |  0 |1|
print(nesting[1]) # 2
print(nesting[2][1])  # 'jaya'
print(nesting[4][1][0]) # True
print(nesting[4][0][0]) # access different characters in the string = 'g'

#Sorting Tuple
nilai = (1,4,3,2,3,6,4,7,7,4,3,3,7,3,3,5,8)
print(sorted(nilai))

#find index
print(number.index("df"))

print("\nINI BATAS\n")

#LIST represented with square bracket []
print("LIST \n")
L = ["mantap", 2, 3.0, True]
print(L)

#len command on list
print(len(L))

#Accessing element on list using index
print(L[0])
print(L[-1])

#Slicing List
print(L[2:5]) #show third - fourth element from L

#Concanate or Adding element on the list
L1 = L + ["bagus", 5, 9.9]
print(L1)

#LIST : MUTABLE
L.extend(["bagus", 5, 9.9]) #add 3 elements to the list
print(L)

L.append(["jaya", 7, 3.4]) #adding elements to the list as one index
print(L)

L[0]="mantap jiwa" #change element on the list, index 0
print(L)

del(L[-1]) #delete the last element of list L
print(L)


#Convert string to list
print("mantap jiwa".split()) #convert string to list
print("A,B,C".split(",")) #separate strings on a spesific character

#Clone list
L2 = [1,2,3]
L3 = L2[:] #clone list L2 to L3
print(L2, L3)
L3[0] = 5
print(L2, L3)
L2[0] = 9 
print(L2, L3)

#help(L) #to get more info of the list/tuple