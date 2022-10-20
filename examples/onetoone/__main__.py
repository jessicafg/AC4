# coding=utf-8

from .mobile import Mobile
from .user import User
from ..common.base import session_factory


def populate_database():
    session = session_factory()

    Matheus = User("Matheus Oliveira")
    Roberta = User("Roberta Larissa")

    Matheus_mobile = Mobile("Android", "958616111", Matheus)
    Roberta_mobile = Mobile("Iphone", "911161685", Roberta)

    session.add(Matheus_mobile)
    session.add(Roberta_mobile)

    session.commit()
    session.close()


def query_users():
    session = session_factory()
    users_query = session.query(User)
    session.close()
    return users_query.all()


def query_mobiles():
    session = session_factory()
    mobiles_query = session.query(Mobile)
    session.close()
    return mobiles_query.all()


if __name__ == "__main__":
    users = query_users()
    if len(users) == 0:
        populate_database()

    users = query_users()
    for user in users:
        print(f'{user.name} has an {user.mobile.model} with number {user.mobile.number}')
