from typing import List

from .router import router
from src.schemas import CategoryForm, CategoryDetail


categories = [
    {'id': 1, 'name': 'Coffee', 'slug': 'coffee'},
    {'id': 2, 'name': 'Tea', 'slug': 'tea'},
]


@router.get('/category', response_model=List[CategoryDetail], name='category list')
async def category_list():
    return [CategoryDetail(**category) for category in categories]

