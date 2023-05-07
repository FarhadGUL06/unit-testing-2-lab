#TODO Creati o baza de date fake ce contine minim 500 de intrari. 
# O intrare este reprezentata de o instanta a clasei Person (pe care trebuie sa o creati) 
# care are minim 3 atribute (nume, varsta, email). Cheia unica este representata de adresa de mail. 

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def __str__(self):
        return f"{self.name} {self.age} {self.email}"

# Generate random number between 20 and 60
import random
def rand():
    return random.randint(20, 60)

# Database
persons = []


def add_pearsons():
    for i in range(501):
        persons.append(Person(f"Name{i}", rand(), f"email{i}@ocw.pub.ro"))

def get_persons_by_email(email):
    for person in persons:
        if person.email.lower() == email.lower():
            return person
    raise ValueError("No person with this email")

# Adaugam persoanele

def generate_database():
    add_pearsons()
    return persons

