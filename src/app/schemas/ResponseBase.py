from pydantic import BaseModel

class ResponseBase(BaseModel):
    """Base schema for API responses."""
    message: str
    status: int

