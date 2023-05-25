from datetime import datetime

from jinja2 import Environment, PackageLoader, Template
from pydantic import BaseModel


class Category(BaseModel):
    name: str
    is_published: bool


objs = [Category(name=f'Category {i}', is_published=True if i % 2 else False) for i in range(10)]
loader = PackageLoader('app')
env = Environment(loader=loader)
template = env.get_template('index.html')
print(template.render())