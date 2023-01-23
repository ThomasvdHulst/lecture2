people = [
    {"name": "Harry", "house": "Griffendor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Drace", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)

