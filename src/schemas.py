from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, root_validator
import ujson


class CategoryForm(BaseModel):
    name: str = Field(
        ...,
        max_length=64,
        title='Category name',
        description=' Unique Category Name'
    )

    class Config:
        json_dumps =ujson.dumps
        json_loads =ujson.loads
        title = 'Category'
        schema_extra = {
            'name': 'Category Name'
        }


class CategoryDetail(CategoryForm):
    id: Optional[PositiveInt]
    slug: str = Field(..., max_length=64)

    @root_validator(pre=True)
    def validator(cls, values: dict) -> dict:
        if not values.get('slug'):
            values['slug'] = values.get('name')
            return values


    class Config:
        json_dumps =ujson.dumps
        json_loads =ujson.loads
        title = 'Category'
        schema_extra = {
            'id': 1,
            'name': 'Category Name',
            'slug': 'category-name'
        }
        orm_mode = True


