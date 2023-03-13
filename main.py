from sqlalchemy import create_engine, select, or_, and_, any_, all_
from sqlalchemy.orm import sessionmaker

from models import Category


engine = create_engine('postgresql://student:password@localhost:5432/homework')
session = sessionmaker(bind=engine)
# with session() as s:
#     cat = Category(name ='Beer')
#     s.add(cat)
#     s.commit()
#     s.refresh(cat)
#     print(cat.pk, cat.name)

with session() as s:
    # cat =  s.get(Category, 1)
    # print(cat.name)
    objs = s.scalars (
        select(Category)
        .order_by(Category.name.desc())
        # .filter(
        #     or_(Category.pk > 0, Category.name.like('%ee%'))
        # )
        # .filter_by()
        # .limit(1)
        # # .offset(2)
    )
    print(objs.all())