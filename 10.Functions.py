#Function (def function_name(variable):)

#Single Parameter
#function add1 >> add 1 to a and store in b
def add1(a):
    """
    add 1 to a_function 
    """ #Documentation string link to help()
    b = a+1
    return b

c = add1(5) #call function add()
print(c) # 6
d = add1(989)
print(d) #990
help(add1) #add1(a) >> add 1 to a_function

#Multi Parameter

#INTEGER
def mult1(e,f):
    g = e * f
    return g
h = mult1(5,6)
print(h)#30

#Different DATA TYPE
def mult1(x,y):
    z = x * y
    return z
u = mult1(2,"abc")
print(u)#abcabc

#no return
def MJ1():
    print('Michael Jackson')
    return(None)