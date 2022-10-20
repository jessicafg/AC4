from datetime import date

from .person import Person
from ..common.base import session_factory


def create_people():
    session = session_factory()
    Matheus = Person("Matheus Oliveira", date(1998, 11, 4), 174, 94.7)
    Roberta = Person("Roberta Larissa", date(1999, 10, 6), 170, 58)
    session.add(Matheus)
    session.add(Roberta)
    session.commit()
    session.close()


def get_people():
    session = session_factory()
    people_query = session.query(Person)
    session.close()
    return people_query.all()


if __name__ == "__main__":
    people = get_people()
    if len(people) == 0:
        create_people()
    people = get_people()

    for person in people:
        print(f'{person.name} was born in {person.date_of_birth}')
