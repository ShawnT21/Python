class Restaurant ():
    """ A description of a restaurant. """
    def  __init__(self, restaurant_name , cuisine_type):
        """ Initializatize restaurant and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def  describe_restaurant(self):
        """ Describe the restaurant"""
        print(self.restaurant_name.title() + " serves " + self.cuisine_type.title() + ".")

    def set_number_served(self):
        """Show customers that have been serverd"""
        print(" The restaurant has served: " + str(self.number_served) + " customers.")

    def increment_number_served(self,served):
        """ Add number of served guest to number served"""
        self.number_served += served

    def  open_restaurant(self):
      """ The Restaurant is open"""
      print(self.restaurant_name.title() + " is now open for business!")

class IceCreamStand():
    """ Simple description an Ice cream chain."""


    def __init__(self, restaurant_name , cuisine_type):
       """
       Initialize attributes of the parent class.
       The Initialize attributes specific to ice cream stand.
       """

     super().__init__( restaurant_name, cuisine_type)
           self.flavors = flavors

   def describe_flavors(self, flavors):
        """Ice cream flavors"""
        print("Ice cream flavors offered:" + self.flavors)

my_restaurant = IceCreamStand('ice cream', 'many flavors')
print(my_restaurant.get_descriptive_name())
print(describe_flavors('chocolate'))


restaurant = Restaurant('Hi',' Japanese')
restaurant.describe_restaurant()

restaurant.number_served = 0
restaurant.set_number_served()

restaurant.increment_number_served(20)
restaurant.set_number_served()

restaurant.open_restaurant()


print("\nThe restaurant is called :" +  restaurant.restaurant_name.title())
print("The restaurant serves :" + restaurant.cuisine_type + " cuisine ")

restaurant = Restaurant('Hola', ' Tex-Mex')
restaurant.describe_restaurant()

print("\nThe restaurant is called :" +  restaurant.restaurant_name.title())
print("The restaurant serves :" + restaurant.cuisine_type + " cuisine ")

restaurant = Restaurant('LOL', ' Mexican')
restaurant.describe_restaurant()

print("\nThe restaurant is called :" +  restaurant.restaurant_name.title())
print("The restaurant serves :" + restaurant.cuisine_type + " cuisine ")

restaurant = Restaurant('Yo', ' American')
restaurant.describe_restaurant()

print("\nThe restaurant is called :" +  restaurant.restaurant_name.title())
print("The restaurant serves :" + restaurant.cuisine_type + " cuisine ")
