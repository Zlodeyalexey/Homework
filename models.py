from sqlalchemy import Column, INT, VARCHAR, DECIMAL, BOOLEAN, ForeignKey
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True)

cat = Category(name='cofee')


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
    def save(self, session: Session = None)-> None:
        session.add(self)
        session.commit()
        session.refresh(self)

    @classmethod
    @create_session
    def get(cls, pk, session: Session = None):
        return session.get(cls, pk)

    @create_session
    def delete(self, session: Session =None):
        session.delete(self)
        session.commit()

    @classmethod
    @create_session
    def scalars(cls, sql, session: Session = None):
        return session.scalars(sql).all()

    @classmethod
    @create-session
    def execute(cls, sql, session: Session = None):
        return session.execute(sql).all()

    def dict(self):
        data = self.__dict__
        data['id'] = data['pk']
        del data['pk']
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


class Category(Base):
name = Column(VARCHAR(64), nullable=False, unique=True)


class Product(Base):
    name = Column(VARCHAR(128), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    descr = Column(VARCHAR(4096), nullable=True)
    is_published = Column(BOOLEAN, default=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)

    @property
    def category(self):
        with self.session() as session:
            return session.get(Category, self.category_id)





