from sqlalchemy import create_engine, select, or_, and_, any_, all_, update, delete
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

# with session() as s:
#     # cat =  s.get(Category, 1)
#     # print(cat.name)
#     objs = s.scalars (
#         select(Category)
#         .order_by(Category.name.desc())
#         # .filter(
#         #     or_(Category.pk > 0, Category.name.like('%ee%'))
#         # )
#         # .filter_by()
#         # .limit(1)
#         # # .offset(2)
#     )
#     print(objs.all())


# with session() as s:
    # s.execute(
    #     update(Category)
    #     .filter(Category.pk == 1)
    #     .values(name='Meat')
    # )
    # s.commit()
    # obj = s.get(Category, 1)
    # obj.name = 'Beer'
    # s.add(obj)
    # s.commit()

    # with session() as s:
    #     # obj = s.ger(Category, 1)
    #     # s.delete(obj)
    #     # s.commit()
    #     s.execute(
    #         delete(Category)
    #         .filter(Category.pk >= 5, Category.pk <= 10)
    #     )
    #     s.commit()