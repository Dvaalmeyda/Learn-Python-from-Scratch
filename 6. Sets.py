#SETS = type collection like lists and tuples but UNORDERED & only have unique elements
#NO DUPLICATE ELEMENTS

set1 = {1,2,3,1,4,1,5,2,3,5,6,7,1}
print(set1) #{1,2,3,4,5,6,7}

#convert list into a set

#use command set
list1 = [1,2,3,1,4,1,5,2,3,5,6,7,1]
print(list1)
set2 = set(list1)
print(set2)

#direct
set3 = ([1,2,3,1,4,1,5,2,3,5,6,7,1])
print("ini set3", set3)

#Set Operations : venn diagram
set_op_a = {"a","b","c","d"}
set_op_b = {"c","d","e","f"}

#add & remove
set_op_a.add("g") #use .add() to add new element. ONLY ONE ARGUMENT 
print("add g to set_op_a", set_op_a)
set_op_a.remove("g")
print("remove g from set_op_a", set_op_a)

#use in to check if the item is in the set
"a" in set_op_a #returns True
"z" in set_op_a #returns False

#Mathematical set operations
set_op_a
set_op_b

#1. INTERSECTION (& or .intersection())
#&
set_op_c = set_op_a & set_op_b
print(set_op_c) #{'c','d'}

#.intersection()
print(set_op_a.intersection(set_op_b)) #{'c','d'}

#2. UNION (.union())
print(set_op_a.union(set_op_b)) #all item from set a and set b

#3. CONFIRM SUPERSET (.issuperset()) & SUBSET (.issubset())
#.issuperset()
print(set_op_a.issuperset(set_op_c))#True
print(set_op_c.issuperset(set_op_a))#False

#.issubset()
print(set_op_c.issubset(set_op_a)) #True
print(set_op_b.issubset(set_op_a)) #False

#4. DIFFERENCE (.difference())
print(set_op_a.difference(set_op_b)) #{'a','b'}
print(set_op_b.difference(set_op_a)) #{'e','f'}