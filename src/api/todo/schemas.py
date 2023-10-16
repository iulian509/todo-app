from pydantic import BaseModel, ConfigDict


class TodoBaseSchema(BaseModel):
    title: str
    priority: int


class TodoCreateSchema(TodoBaseSchema):
    pass


class TodoUpdateSchema(TodoBaseSchema):
    pass


class TodoSchema(TodoBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
