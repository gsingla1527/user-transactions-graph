from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class UserCreate(BaseModel):
    user_id: str = Field(..., description="Unique user ID")
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    payment_method: Optional[str] = None


class TransactionCreate(BaseModel):
    tx_id: str = Field(..., description="Unique transaction ID")
    from_user: str
    to_user: str
    amount: float
    currency: str = "USD"
    timestamp: datetime
    ip: Optional[str] = None
    device_id: Optional[str] = None


class RelationshipEdge(BaseModel):
    source: str
    target: str
    type: str


class Node(BaseModel):
    id: str
    label: str
    kind: str  # "user" or "transaction"


class GraphResponse(BaseModel):
    nodes: List[Node]
    edges: List[RelationshipEdge]
