from typing import Optional

from pydantic import BaseModel


class StaskAdd(BaseModel):
    name: str
    description: Optional[str] = None
    
class Stask(StaskAdd):
    id: int
    
    
class StaskId(BaseModel):
    ok: bool = True
    task_id: int