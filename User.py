from sqlalchemy import Column, INT, VARCHAR, ForeignKey, CASSCADE, BOOLEAN
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker
from asqlalchemy import TIMESTAMP
from pydantic import BaseModel, Field
from sqlalchemy.sql.functions import now
from pydantic.types import Decimal


class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True)

    engine = create_engine(///////////)
    session = sessionmaker(bind=engine)


class User(Base):
    name = Column(VARCHAR(255), nullable=False)

class Chat(Base):
    name = Column(VARCHAR(255), nullable=False)

class Chat_member(Base):
    chat_id = Column(INT), ForeignKey('Chat.id', ondelete='CASSCADE'), nullable=False)


class User_id(Base):
    chat_id = Column(INT), ForeignKey('Chat.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(INT), ForeignKey('User.id', ondelete='CASSCADE'), nullable=False)

class Message(Base):
    chat_id = Column(INT), ForeignKey('Chat.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(INT), ForeignKey('User.id', ondelete='CASSCADE'), nullable = False)
    text =Column(VARCHAR(1024), nullable=False)
    date_created =Column(TIMESTAMP)