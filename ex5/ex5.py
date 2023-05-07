# TODO Creati un stub si o functie fake care sa simuleze 
# functionalitatea metodei get(cheie_unica) pe o baza de date. 
# Puteti sa folositi baza de date creata anterior. 

from ex4 import generate_database, get_persons_by_email

persons = generate_database()

def get_person(email):
    person = get_persons_by_email(email)
    return person

# Test get_person
print("Email: ", get_person("email1@ocw.pub.ro").name, "Age: ", get_person("email1@ocw.pub.ro").age)
