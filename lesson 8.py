from pydantic import BaseModel, EmailStr, Field, validator, root_validator


class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=18, lt=65)
    email: EmailStr = None
    password: str = Field(min_length=8)

    # @validator('password')
    # def validate_password(cls, value):
    #     pass
    @root_validator
    def validate_values(cls, values):
        if values.get('name').lower() in values.get('password').lower():
            raise ValueError('имя не должно содержаться в пароле')
        return values


try:
    vasya = User(name='vasya', age=19, email='vasya@info.com', password='qwerVaSyAtyuiop')
    print(vasya.dict())
except Exception as e:
    print(e)