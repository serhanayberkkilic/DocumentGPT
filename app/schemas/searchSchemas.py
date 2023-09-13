from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID



# Shared properties
class Base(BaseModel):
    text: Optional[str]=Field(description="Text",max_length=200)


# Properties to receive on device creation
class Create(Base):
    text: str=Field(description="Text",max_length=200)


