from pydantic import BaseModel,field_validator,Field,field_serializer
import re

class BaseCostSchema(BaseModel):
    description : str
    price : float
   
    @field_validator("description")
    def validate_description(cls,value):
        if len(value) > 35:
            raise ValueError("Description must not exceed 35 charecters")
        if not value.isalpha():
            raise ValueError("Description must contain only charecters")
        return value

    @field_validator("price")
    def check_value_range(cls, value):
        if not (0.01 <= value <= 10000000.0):
            raise ValueError('Value must be between 0.01 and 10000000.0')
        return value

    @field_serializer("description")
    def serialize_name(value):
        return value.title()

    @field_serializer("price")
    def serialize_float(self,value):
        return round(value,2)
    
class CostsCreateSchema(BaseCostSchema):
    pass

class CostsResponseSchema(BaseCostSchema):
    id : int = Field(...,description="Unique user identifier")

class CostsUpdateSchema(BaseCostSchema):
    pass