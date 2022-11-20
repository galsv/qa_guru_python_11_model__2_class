from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender = Gender.Male.value
    name: str = 'Ivan'
    last_name: str = 'Ivanov'
    email: str = 'ivanov_ivan@test.test'
    user_number: str = '0123456789'
    date: str = '10 Oct 1984'
    subjects: Tuple[Subject] = (Subject.History,)
    current_address: str = 'bla bla bla'
    hobbies: Tuple[Hobby] = (Hobby.Sports,)
    picture_file: str = 'test.png'
    state: str = 'NCR'
    city: str = 'Delhi'

user = User()