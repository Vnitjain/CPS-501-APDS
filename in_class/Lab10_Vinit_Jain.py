# Name: Vinit Jain
# Date: 2023-11-08
# Assignment: Lab 10
# Class: CPS 501


# Question 1: Defining a Base Class
# Define a class Vehicle with properties like make, model, and year. Use self in __init__
# Create a method display_info() that prints out this information.


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # printing out the information in a single string
        print(
            "Make: "
            + self.make
            + "\nModel: "
            + self.model
            + "\nYear: "
            + str(self.year)
        )


# Example Usage
v = Vehicle("Toyota", "Corolla", 2020)
v.display_info()

# Question 2: Simple Inheritance
# Define a class Car that inherits from Vehicle and adds a property wheels with a default value of 4. (How does a class inherit from another class)
# Override the display_info() method to include the number of wheels. (i.e. what else needs to be added to display_info)


class Car(Vehicle):
    # creating constructor and adding wheels to it and set a default value
    def __init__(self, make, model, year, wheels=4):
        super().__init__(make, model, year)
        self.wheels = wheels

    # Default values go here
    def display_info(self, wheels=4):
        super().display_info()
        print("Wheels: " + str(wheels))


# Example Usage
c = Car("Honda", "Civic", 2019)
c.display_info()


# Question 3: Constructor Chaining
# Define a class ElectricCar that inherits from Car. Add a new property battery_size. Ensure that the constructor properly uses super() to initialize the inherited properties.
# Polymorphism and Dynamic Behavior


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        # setting the battery size along with other properties
        self.battery_size = battery_size


# Example Usage
ec = ElectricCar("Tesla", "Model 3", 2021, "75kWh")
ec.display_info()
print(f"Battery size: {ec.battery_size}")


# Question 4: Method Overriding
# Demonstrate method overriding by defining a method charge() in both Vehicle (doing nothing or raising a NotImplementedError)
# and ElectricCar (where it actually performs a relevant action, like updating a battery_level attribute).
# Instantiate electriccar and print charge


class Vehicle:
    # ... (other methods and properties)

    def charge(self):
        raise NotImplementedError("This method should be overridden by subclasses.")


class ElectricCar(Car):
    # ... (other methods and properties)

    def charge(self):
        # setting the battery level while overriding the charge method
        self.battery_level = 100
        print("Charge: " + str(self.battery_level) + "%")


# Example Usage
ec = ElectricCar("Tesla", "Model S", 2022, "100kWh")
ec.charge()


# Question 5: Multiple Inheritance
# Two base classes are defined: Electric and Hybrid, with their own unique methods and properties.
# Create a class HybridElectricCar that inherits from both and call both functions that are inherited.


class Electric:
    def charge(self):
        print("Charging electric component.")


class Hybrid:
    def fill_tank(self):
        print("Filling the tank.")


class HybridElectricCar(Electric, Hybrid):
    pass


# Example Usage - call both functions here
hec = HybridElectricCar()
# calling both the inherited methods
hec.charge()
hec.fill_tank()

# Question 7b: Multiple inheritance. Which method gets called from C?
# Answer: It will call the method that is inherited most recently, in this case its do_something() in class B


class A:
    def do_something(self):
        print("Method defined in A")


class B(A):
    def do_something(self):
        print("Method defined in B")


class C(B, A):
    pass


# Example usage
c_instance = C()
c_instance.do_something()
