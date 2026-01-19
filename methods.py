import datetime

class Person:
    # This is a class attribute, shared by all instances
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 1. Instance Method: Needs 'self' to access instance data
    def display_details(self):
        """Prints the details of this specific person."""
        print(f"Name: {self.name}, Age: {self.age}, Species: {self.species}")

    # 2. Class Method: A factory to create a Person from a birth year
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Creates a Person instance by calculating their age from their birth year."""
        current_year = datetime.date.today().year
        age = current_year - birth_year
        # 'cls' here is the Person class. This creates an instance of Person.
        return cls(name, age)

    # 3. Static Method: A utility function related to the class
    @staticmethod
    def is_adult(age):
        """Checks if a given age is considered adult."""
        return age >= 18

# --- How to use them ---

# Create an instance the standard way
person1 = Person("Yash", 21)
# Call the instance method
person1.display_details()
# Output: Name: Yash, Age: 21, Species: Homo sapiens

# Create an instance using the class method factory
person2 = Person.from_birth_year("Aisha", 2000)
# Call the instance method on the new object
person2.display_details()
# Output: Name: Aisha, Age: 25, Species: Homo sapiens

# Call the static method directly from the class
can_vote = Person.is_adult(25)
print(f"Is a 25-year-old an adult? {can_vote}")
# Output: Is a 25-year-old an adult? True