students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])

pupils = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
    }

for pupil in pupils:
    print(pupil, pupils[pupil], sep=", ")

for pupil,house in pupils.items():
    print(pupil, house)


opiskelijat = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for opiskelija in opiskelijat:
    print(opiskelija["name"], opiskelija["house"], opiskelija["patronus"], sep=", ")