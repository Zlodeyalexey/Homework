from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Category


engine = create_engine('postgresql://login:password@localhost:5432/data')
session = sessionmaker(bind=engine)
# with session() as s:
#     cat = Category(name='Beer')
#     s.add(cat)
#     s.commit()
#     s.refresh(cat)
#     print(cat.pk, cat.name)

with session() as s:
#     cat = s.get(Category, 1)
#     print(cat.name)
    objs = s.scalars(
        select(Category)
        .order_by(Category.name.desc())
        .limit(1)
        .offset(2)
        .filter()
        .where()
        .filter_by()
    )
