from typing import TypedDict

class Person(TypedDict):
    name : str
    age: int

new_person: Person = {'name':'Saurabh', 'age':25}

# Here we're passing age as string, still no error in TypedDict:
# new_person: Person = {'name':'Saurabh', 'age':'25'}

print(new_person)