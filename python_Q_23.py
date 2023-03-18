"""
Q-23:PizzaForYou is a pizza store which sells different kinds of pizzas based on customer's order.40 min.Customer can either collect the order in person or opt for a door delivery.Write a
python program based on the class diagram given below.

RULLS TO FOLLOW:-
Customer class:
 validate_quantity(): A customer can order 1 to 5 pizzas
 If quantity is valid, return true. Else return false
Pizzaservice class:
 Initialize static variable counter to 100
  Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.
  True – additional topping is required, False – additional topping is not required
validate_pizza_type():
  Customers can order "small" or "medium" type pizzas
If pizza type is valid, return true. Else return false
calculate_pizza_cost(): Calculate pizza cost
    Validate pizza type and quantity
  If valid,
  Identify pizza cost based on details mentioned in the table Set attribute, pizza_cost with the calculated pizza cost Auto-generate service_id starting from 101 prefixed by first letter
  of pizza type.
  Example – S101, s102, m103, S104, M105 etc
 If invalid, set pizza_cost to -1
 PizzaType	Cost/Pizza(in Rs)	Additional topping cost/Pizza(in Rs), if applicable
  Small	             150                	35
  Medium	     200	                50
Doordelivery class:
 validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms
 Validate distance_in_kms
 If valid, return true. Else, return false
 calculate_pizza_cost: Calculate pizza cost
 Validate distance in kms
 If valid,
 Calculate pizza cost (Hint: Invoke overridden method in parent class)
If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost
Distance in kms	     Delivery Charge in km(in Rs)
 For first 5 kms	    5
 For remaining 5 kms	    7
Else, set pizza_cost to -1
Note: Perform case insensitive string comparison  
For testing:
 Create objects of Pizzaservice and Doordelivery classes
 Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
 Display the details.
"""
types=['small','medium','small','medium']
class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else:
            return False
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity
    
class Pizzaservice:
    counter=100 #it is counter which is static
    def __init__(self, customer, pizza_type, additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__service_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in types:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer.validate_quantity(self.__customer):
            print("pizza")
            if self.__pizza_type == "small":
                self.pizza_cost=150 * Customer.get_quantity(self.__customer)
                if self.__additional_topping:
                    self.pizza_cost+=35 * Customer.get_quantity(self.__customer)
            if self.__pizza_type == "medium":
                self.pizza_cost=200 * Customer.get_quantity(self.__customer)
                print("hi")
                if self.__additional_topping:
                    self.pizza_cost+=50 * Customer.get_quantity(self.__customer)
            if not self.__service_id:
                self.__service_id = self.__pizza_type[0] +str(Pizzaservice.counter+1)
                Pizzaservice.counter+=1
        else:
            self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping
    
class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        self.__delivery_charge=0
        self.__distance_in_kms=distance_in_kms
        Pizzaservice.__init__(self, customer, pizza_type, additional_topping)
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost!= -1:
                distance=1
    
                while(distance<=self.__distance_in_kms):
                    if distance in range(1,6):
                        self.pizza_cost += 5
                    if distance in range(6,11):
                        self.pizza_cost += 7
                    distance += 1
        else:
            self.pizza_cost = -1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms
c = Customer("Lisha", 5)
print(c.get_customer_name())
p1 = Pizzaservice(c, "medium", True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())

d1 = Doordelivery(c, "medium", True,6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())
