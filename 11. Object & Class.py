#OBJECT 
#Every object has : 
# 1. Type
# 2. Internal data representation (blueprint)
# 3. Procedure/Function for interacting with the object (method)


class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1
make="BMW"
model="M3"
color="red"
        
my_car = Car(make, model, color)

my_car.car_info()

for i in range(5):
    my_car.sell()

my_car.car_info()

A = ['1','2','3']

for a in A:

print(2*a)