# This Python script demonstrates Object-Oriented Programming (OOP) concepts
# including classes, attributes, methods, inheritance, and polymorphism.

# --- Assignment 1: Design Your Own Class ---

class Weapon:
    """
    A base class representing a generic weapon.
    This class has a constructor to initialize its attributes and a method for its action.
    """

    def __init__(self, name: str, damage: int, rarity: str):
        """
        Constructor for the Weapon class.
        Initializes the weapon's name, damage, and rarity.
        
        Args:
            name (str): The name of the weapon.
            damage (int): The base damage the weapon inflicts.
            rarity (str): The rarity of the weapon (e.g., "Common", "Rare").
        """
        self.name = name
        self.damage = damage
        self.rarity = rarity

    def attack(self):
        """
        A method to perform a generic attack action.
        """
        print(f"The {self.name} attacks, dealing {self.damage} damage.")

class Sword(Weapon):
    """
    A subclass of Weapon representing a sword.
    This class adds a unique attribute (blade_length) and overrides the attack method.
    This demonstrates inheritance and polymorphism.
    """

    def __init__(self, name: str, damage: int, rarity: str, blade_length: float):
        """
        Constructor for the Sword class.
        It calls the parent class's constructor and adds a new attribute.
        
        Args:
            name (str): The name of the sword.
            damage (int): The base damage.
            rarity (str): The rarity.
            blade_length (float): The length of the blade in inches.
        """
        super().__init__(name, damage, rarity)
        self.blade_length = blade_length

    def attack(self):
        """
        Overrides the parent's attack method to provide a unique action for a sword.
        """
        print(f"The {self.name} slashes, dealing {self.damage} slashing damage with its {self.blade_length}-inch blade.")

class Bow(Weapon):
    """
    A subclass of Weapon representing a bow.
    It adds a unique attribute (arrow_type) and a new method (aim).
    """

    def __init__(self, name: str, damage: int, rarity: str, arrow_type: str):
        """
        Constructor for the Bow class.
        
        Args:
            name (str): The name of the bow.
            damage (int): The base damage.
            rarity (str): The rarity.
            arrow_type (str): The type of arrows used (e.g., "Fire", "Poison").
        """
        super().__init__(name, damage, rarity)
        self.arrow_type = arrow_type

    def aim(self):
        """
        A unique method for the Bow class.
        """
        print(f"Aiming the {self.name} with a {self.arrow_type} arrow...")
        
    def attack(self):
        """
        Overrides the parent's attack method to provide a unique action for a bow.
        """
        print(f"The {self.name} fires a {self.arrow_type} arrow, dealing {self.damage} piercing damage.")


# --- Assignment 2: Polymorphism Challenge ---

class Vehicle:
    """
    A base class for different types of vehicles.
    """
    def move(self):
        """
        A generic move method.
        """
        raise NotImplementedError("Subclasses must implement the 'move' method.")

class Car(Vehicle):
    """
    A Car class that moves by driving.
    """
    def move(self):
        """
        Implements the move action for a Car.
        """
        print("Driving 🚗")

class Plane(Vehicle):
    """
    A Plane class that moves by flying.
    """
    def move(self):
        """
        Implements the move action for a Plane.
        """
        print("Flying ✈️")

class Boat(Vehicle):
    """
    A Boat class that moves by sailing.
    """
    def move(self):
        """
        Implements the move action for a Boat.
        """
        print("Sailing ⛵️")

def perform_move(vehicle: Vehicle):
    """
    A function that takes a Vehicle object and calls its move() method.
    This demonstrates polymorphism.
    """
    vehicle.move()

# --- Main execution of the script ---

if __name__ == "__main__":
    print("--- Assignment 1: Weapon Class Hierarchy ---")
    
    # Create objects from the classes
    iron_sword = Sword("Iron Sword", 15, "Common", 30.5)
    fire_bow = Bow("Fire Bow", 25, "Rare", "Fire")
    
    # Call methods and access attributes
    print(f"Weapon 1: {iron_sword.name}, Rarity: {iron_sword.rarity}")
    iron_sword.attack()
    print("-" * 20)
    
    print(f"Weapon 2: {fire_bow.name}, Rarity: {fire_bow.rarity}")
    fire_bow.aim()
    fire_bow.attack()
    print("\n")

    print("--- Assignment 2: Polymorphism Challenge ---")

    # Create objects from the vehicle classes
    my_car = Car()
    my_plane = Plane()
    my_boat = Boat()

    # Call the polymorphic function with different vehicle types
    perform_move(my_car)
    perform_move(my_plane)
    perform_move(my_boat)
