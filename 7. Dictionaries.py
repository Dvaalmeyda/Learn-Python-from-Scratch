#DICTIONARIES = type of collection, use curly bracket {}
#List = (index & element) ; Dictionaries (key & value)
#The keys can be character but it have to be immutable & unique
#key can also be any immutable object such as a tuple

#Dictionaries of movies and release data
D1 = {"Avatar 2" : 2022, "Avengers : Infinity Wars" : 2020, "Thriller" : 1982}
print(type(D1)) #dictionaries (dict)
print(D1)

#Accessing the key will return the value
print(D1["Avatar 2"])

#Add new entry to dictionary (Dictionary[key]=value)
D1["Graduation"]=2007
print(D1)

#Delete entry (del([]))
del(D1["Graduation"])
print(D1)

#Verify element ("key in Dictionary names")
print("Avatar 2" in D1)#returns True
print("Fight Club" in D1) #returns False

#See all keys on dictionary (.keys())
print(D1.keys())#dict_keys(['key name'])

#See all values on dictionary (.values())
print(D1.values())#dict_values(['value name'])