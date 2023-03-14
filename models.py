from pydantic.types import Decimal
from sqlalchemy import Column, INT, VARCHAR, DECIMAL, BOOLEAN, ForeignKey, create_engine
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, Session

from pydantic import BaseModel, EmailStr, Field, validator, root_validator
from sqlalchemy.sql.functions import now



class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True)

    engine = create_engine('postgresql://student:password@localhost:5432/homework')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with Base.session() as session:
                return func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    def save(self, session: Session = None) -> None:
        session.add(self)
        session.commit()
        session.refresh(self)

    @classmethod
    @create_session
    def get(cls, pk, session: Session = None):
        return session.get(cls, pk)

    @create_session
    def delete(self, session: Session = None):
        session.delete(self)
        session.commit()

    @classmethod
    @create_session
    def scalars(cls, sql, session: Session = None):
        return session.scalars(sql).all()

    @classmethod
    @create_session
    def execute(cls, sql, session: Session = None):
        return session.execute(sql).all()

    def dict(self):
        data = self.__dict__
        data['id'] = data['pk']
        del data['pk']
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


# class Category(Base):,

import csv

# users = [
#     {'name': 'user1', 'email': 'user1@mail.com'},
#     {'name': 'user2', 'email': 'user2@mail.com'},
#     {'name': 'user3', 'email': 'user3@mail.com'},
# ]
with open('users.csv','r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['email'])



