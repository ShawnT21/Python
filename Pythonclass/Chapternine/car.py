class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make+ ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it. ")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")


    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self, fill_gas_tank):
       """Electric cars don't have gas tanks."""
       print("Fill up the tank" + self.fill_gas_tank)

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 85):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = " This car can go appoximately " + str(range)
        message += " miles on a full charge. "
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""


    def __init__(self, make, model, year):
       """
       Initialize attributes of the parent class.
       The Initialize attributes specific to an electric car
       """
       super().__init__(make,model, year)
       self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + " -KWh battery.")

    def fill_gas_tank(self, fill_gas_tank):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!" + self.fill_gas_tank)


my_tesla = ElectricCar('tesla', ' model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
